#!/usr/bin/env python3
"""
Mechanical CoNLL-U metadata edits for the spoken-data metadata-harmonisation
issues (workgroups/spoken-data/issue_drafts/*.md).

Covers the three kinds of changes that recur across nearly every issue draft:

  rename-comment   rename a `# key = value` comment (doc-, sent- or
                   paragraph-level) to a new key name.
  rename-misc      rename a token-level MISC key (10th column, `Key=Value`
                   pairs separated by `|`).
  hoist-to-doc     move a sentence-level comment up to the `# newdoc id`
                   comment of its document, IF the value is constant
                   throughout the document (aborts with a report otherwise -
                   this is the check maintainers were asked to "confirm").
  split-field      split a composite comment value on a separator into
                   several new comments.
  tag-modality     add `# modality = spoken|written` to each document's
                   `# newdoc id` line, based on a regex match against the
                   `newdoc id` value.
  derive-newdoc    insert a `# newdoc id = ...` comment derived from the
                   `sent_id` of each block's first sentence, when no
                   `newdoc id` exists at all.

Every operation is available as `--dry-run` (default) which only prints a
diff-like report; pass `--write` to edit the files in place. Run on one file
or a whole directory (`*.conllu`, recursive).

This does NOT decide *whether* a change is a good idea - that's still a
judgement call for the corpus maintainers. It only removes the mechanical,
error-prone part (editing every comment/column by hand across thousands of
sentences) once the maintainer has confirmed the mapping.

Examples
--------
Rename a sentence-level field everywhere under a treebank directory:
    python harmonize_metadata.py rename-comment DIR --map jefferson_text=text_transcr --write

Rename token-level MISC keys:
    python harmonize_metadata.py rename-misc DIR --map Begin=WordAlignmentBegin,End=WordAlignmentEnd --write

Hoist a constant sentence-level field to document level (checks constancy first):
    python harmonize_metadata.py hoist-to-doc DIR --key sound_url --write

Split a composite field like `fr/female/sp0013f`:
    python harmonize_metadata.py split-field DIR --key speaker --sep / \
        --into speaker_variety,speaker_gender,speaker_id --write

Tag modality from a newdoc-id pattern:
    python harmonize_metadata.py tag-modality DIR \
        --spoken-if '^(conversation|film)' --written-if '^(book|grammar)' --write

Derive newdoc id from sent_id prefix (e.g. Rhap_D0001-1 -> Rhap_D0001):
    python harmonize_metadata.py derive-newdoc DIR --pattern '^(?P<doc>.+)-\\d+$' --write
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COMMENT_RE = re.compile(r"^#\s*([^=\n]+?)\s*=\s*(.*)$")


def find_conllu_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.conllu"))


def iter_docs(lines: list[str]):
    """Yield (start, end) index ranges (half-open) for each `newdoc`-delimited
    block. If there is no `newdoc` comment at all, the whole file is one doc."""
    starts = [i for i, l in enumerate(lines) if l.startswith("# newdoc")]
    if not starts:
        yield 0, len(lines)
        return
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(lines)
        yield s, e


def iter_sents(lines: list[str], start: int, end: int):
    """Yield (start, end) ranges for each sentence block (comments + tokens)
    within [start, end)."""
    sent_starts = [i for i in range(start, end) if lines[i].startswith("# sent_id")]
    if not sent_starts:
        yield start, end
        return
    for i, s in enumerate(sent_starts):
        e = sent_starts[i + 1] if i + 1 < len(sent_starts) else end
        yield s, e


def report(msg: str):
    print(msg)


def write_back(path: Path, lines: list[str], write: bool, changed: bool):
    if changed and write:
        path.write_text("".join(lines), encoding="utf-8")
        report(f"  wrote {path}")
    elif changed:
        report(f"  (dry-run, no changes written to {path})")


def cmd_rename_comment(args):
    mapping = dict(pair.split("=", 1) for pair in args.map.split(","))
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        for i, line in enumerate(lines):
            m = COMMENT_RE.match(line.strip("\n"))
            if m and m.group(1) in mapping:
                new_key = mapping[m.group(1)]
                lines[i] = f"# {new_key} = {m.group(2)}\n"
                changed = True
        if changed:
            report(f"{path}: renamed {list(mapping.items())}")
        write_back(path, lines, args.write, changed)


def cmd_rename_misc(args):
    mapping = dict(pair.split("=", 1) for pair in args.map.split(","))
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        for i, line in enumerate(lines):
            if line.startswith("#") or not line.strip() or "\t" not in line:
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) != 10:
                continue
            misc = cols[9]
            if misc == "_":
                continue
            parts = misc.split("|")
            new_parts = []
            local_changed = False
            for p in parts:
                if "=" in p:
                    k, v = p.split("=", 1)
                    if k in mapping:
                        p = f"{mapping[k]}={v}"
                        local_changed = True
                new_parts.append(p)
            if local_changed:
                cols[9] = "|".join(new_parts)
                lines[i] = "\t".join(cols) + "\n"
                changed = True
        if changed:
            report(f"{path}: renamed MISC keys {list(mapping.items())}")
        write_back(path, lines, args.write, changed)


def cmd_hoist_to_doc(args):
    key = args.key
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        for ds, de in iter_docs(lines):
            values = set()
            occurrences = []
            for i in range(ds, de):
                m = COMMENT_RE.match(lines[i].strip("\n"))
                if m and m.group(1) == key:
                    values.add(m.group(2))
                    occurrences.append(i)
            if not occurrences:
                continue
            if len(values) > 1:
                report(f"{path}: SKIP doc at line {ds+1} - `{key}` is NOT constant "
                        f"({len(values)} distinct values) - needs manual review, not hoisted")
                continue
            value = values.pop()
            # remove all per-sentence occurrences
            for i in sorted(occurrences, reverse=True):
                del lines[i]
                de -= 1
            # insert once, right after the newdoc comment (or at doc start)
            insert_at = ds + 1 if lines[ds].startswith("# newdoc") else ds
            lines.insert(insert_at, f"# {key} = {value}\n")
            changed = True
            report(f"{path}: hoisted `{key} = {value}` to document level (doc at line {ds+1})")
        write_back(path, lines, args.write, changed)


def cmd_split_field(args):
    key, sep, into = args.key, args.sep, args.into.split(",")
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        offset = 0
        for i, line in enumerate(list(lines)):
            m = COMMENT_RE.match(line.strip("\n"))
            if not m or m.group(1) != key:
                continue
            parts = m.group(2).split(sep)
            if len(parts) != len(into):
                report(f"{path}: SKIP `{key}` value `{m.group(2)}` - splits into "
                        f"{len(parts)} parts, expected {len(into)} - needs manual review")
                continue
            idx = i + offset
            new_lines = [f"# {name} = {val}\n" for name, val in zip(into, parts)]
            lines[idx:idx + 1] = new_lines
            offset += len(new_lines) - 1
            changed = True
        if changed:
            report(f"{path}: split `{key}` into {into}")
        write_back(path, lines, args.write, changed)


def cmd_derive_newdoc_from_field(args):
    """Insert `# newdoc id` derived from another comment field that is
    already repeated per-sentence (e.g. `text_name`, `sound_url`), one
    insertion per distinct value, at the first sentence carrying it."""
    key = args.key
    suffix = args.strip_suffix
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        if any(l.startswith("# newdoc") for l in lines):
            continue  # already has newdoc ids, nothing to derive
        changed = False
        seen = set()
        offset = 0
        idxs = [i for i, l in enumerate(lines) if COMMENT_RE.match(l.strip("\n")) and COMMENT_RE.match(l.strip("\n")).group(1) == key]
        for i in idxs:
            idx = i + offset
            m = COMMENT_RE.match(lines[idx].strip("\n"))
            value = m.group(2)
            doc_id = value[:-len(suffix)] if suffix and value.endswith(suffix) else value
            if doc_id in seen:
                continue
            seen.add(doc_id)
            lines.insert(idx, f"# newdoc id = {doc_id}\n")
            offset += 1
            changed = True
        if changed:
            report(f"{path}: derived {len(seen)} newdoc id(s) from `{key}`")
        write_back(path, lines, args.write, changed)


def cmd_tag_modality(args):
    spoken_re = re.compile(args.spoken_if) if args.spoken_if else None
    written_re = re.compile(args.written_if) if args.written_if else None
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        for i, line in enumerate(lines):
            m = COMMENT_RE.match(line.strip("\n"))
            if not m or m.group(1) != "newdoc id":
                continue
            value = m.group(2)
            modality = None
            if spoken_re and spoken_re.search(value):
                modality = "spoken"
            elif written_re and written_re.search(value):
                modality = "written"
            if modality is None:
                report(f"{path}: no modality match for newdoc id `{value}` - needs manual tagging")
                continue
            lines.insert(i + 1, f"# modality = {modality}\n")
            changed = True
        if changed:
            report(f"{path}: added modality tags")
        write_back(path, lines, args.write, changed)


def cmd_derive_newdoc(args):
    pattern = re.compile(args.pattern)
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        if any(l.startswith("# newdoc") for l in lines):
            continue  # already has newdoc ids, nothing to derive
        changed = False
        seen_docs = set()
        offset = 0
        sent_id_idxs = [i for i, l in enumerate(lines) if l.startswith("# sent_id")]
        for i in sent_id_idxs:
            idx = i + offset
            m = COMMENT_RE.match(lines[idx].strip("\n"))
            if not m:
                continue
            sent_id = m.group(2)
            pm = pattern.match(sent_id)
            if not pm:
                report(f"{path}: sent_id `{sent_id}` doesn't match pattern - needs manual review")
                continue
            doc_id = pm.group("doc")
            if doc_id in seen_docs:
                continue
            seen_docs.add(doc_id)
            lines.insert(idx, f"# newdoc id = {doc_id}\n")
            offset += 1
            changed = True
        if changed:
            report(f"{path}: derived {len(seen_docs)} newdoc id(s) from sent_id")
        write_back(path, lines, args.write, changed)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("path", help="a .conllu file or a directory (searched recursively)")
        sp.add_argument("--write", action="store_true", help="apply changes in place (default: dry-run report only)")

    sp = sub.add_parser("rename-comment", help="rename a `# key = value` comment")
    common(sp)
    sp.add_argument("--map", required=True, help="old=new[,old2=new2,...]")
    sp.set_defaults(func=cmd_rename_comment)

    sp = sub.add_parser("rename-misc", help="rename a token-level MISC key")
    common(sp)
    sp.add_argument("--map", required=True, help="old=new[,old2=new2,...]")
    sp.set_defaults(func=cmd_rename_misc)

    sp = sub.add_parser("hoist-to-doc", help="move a constant sentence-level field to document level")
    common(sp)
    sp.add_argument("--key", required=True)
    sp.set_defaults(func=cmd_hoist_to_doc)

    sp = sub.add_parser("split-field", help="split a composite comment value into several new comments")
    common(sp)
    sp.add_argument("--key", required=True)
    sp.add_argument("--sep", default="/")
    sp.add_argument("--into", required=True, help="new_key1,new_key2,...")
    sp.set_defaults(func=cmd_split_field)

    sp = sub.add_parser("derive-newdoc-from-field", help="insert `# newdoc id` derived from another repeated comment field")
    common(sp)
    sp.add_argument("--key", required=True, help="the repeated comment field to derive newdoc id from, e.g. sound_url")
    sp.add_argument("--strip-suffix", default="", help="suffix to strip from the value, e.g. .WAV or .eaf")
    sp.set_defaults(func=cmd_derive_newdoc_from_field)

    sp = sub.add_parser("tag-modality", help="add `# modality = spoken|written` from a newdoc-id regex")
    common(sp)
    sp.add_argument("--spoken-if", help="regex matched against newdoc id -> modality=spoken")
    sp.add_argument("--written-if", help="regex matched against newdoc id -> modality=written")
    sp.set_defaults(func=cmd_tag_modality)

    sp = sub.add_parser("derive-newdoc", help="insert `# newdoc id` derived from sent_id prefix")
    common(sp)
    sp.add_argument("--pattern", required=True, help="regex with a (?P<doc>...) group, matched against sent_id")
    sp.set_defaults(func=cmd_derive_newdoc)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
