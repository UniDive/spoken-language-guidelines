#!/usr/bin/env python3
"""
One-off helper for UD_Highland_Puebla_Nahuatl-ITML (issue_drafts item 3):
consolidate the many `# text[a<N>] = ...` per-sentence comments into a
single `# text_original = [a<N>] ... [a<M>] ...` comment, in file order.

Usage:
    python3 consolidate_text_variants.py PATH --pattern 'text\\[(a\\d+)\\]' --into text_original [--write]

Dry-run by default; pass --write to edit files in place.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

COMMENT_RE = re.compile(r"^#\s*([^=]+?)\s*=\s*(.*)$")


def find_conllu_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.conllu"))


def process(lines: list[str], key_re: re.Pattern, into: str):
    changed = False
    i = 0
    while i < len(lines):
        line = lines[i]
        m = COMMENT_RE.match(line.strip("\n"))
        if not m or not key_re.fullmatch(m.group(1)):
            i += 1
            continue
        # gather the contiguous run of matching comments starting here
        run_start = i
        pieces = []
        while i < len(lines):
            mm = COMMENT_RE.match(lines[i].strip("\n"))
            if not mm or not key_re.fullmatch(mm.group(1)):
                break
            km = key_re.fullmatch(mm.group(1))
            label = km.group(1)
            pieces.append(f"[{label}] {mm.group(2)}")
            i += 1
        merged = f"# {into} = " + " ".join(pieces) + "\n"
        lines[run_start:i] = [merged]
        i = run_start + 1
        changed = True
    return changed


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path")
    p.add_argument("--pattern", required=True, help=r"regex with one group capturing the label, matched against the comment key, e.g. 'text\[(a\d+)\]'")
    p.add_argument("--into", required=True, help="new comment key")
    p.add_argument("--write", action="store_true")
    args = p.parse_args()

    key_re = re.compile(args.pattern)
    for path in find_conllu_files(Path(args.path)):
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = process(lines, key_re, args.into)
        if changed:
            print(f"{path}: consolidated matches of /{args.pattern}/ into `{args.into}`")
            if args.write:
                path.write_text("".join(lines), encoding="utf-8")
                print(f"  wrote {path}")
            else:
                print(f"  (dry-run, no changes written to {path})")


if __name__ == "__main__":
    main()
