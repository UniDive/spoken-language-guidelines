---
layout: base
title: 'Issue draft: Nenets Tundra'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Nenets Tundra](../treebanks/UD_Nenets-Tundra.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Nenets-Tundra](https://github.com/UniversalDependencies/UD_Nenets-Tundra)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Nenets-Tundra`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `document_id` exists, but `doc_title_` already identifies the document and can be used directly to introduce it.

| Field        | Suggestion                                                                           |
| ------------ | ------------------------------------------------------------------------------------ |
| `doc_title_` | use as `# document_id` (rename/repurpose the field)                                    |
| `sound_url`  | move to document level |
| `media`      | corpus-specific (doc-level) - verify against metadata.html                           |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion                             |
| ---------- | --------------------------------------- |
| `text_p`   | unclear                                |
| `translit` | change to `text_translitteration`      |
| `p_text`   | unclear, maybe also typo for `text_p`? |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### Implementation notes

**Quick search & replace**
- `translit` → `text_translitteration`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map translit=text_translitteration --write`
- `AlignBegin`/`AlignEnd` → `WordAlignmentBegin`/`WordAlignmentEnd` (token MISC): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`

**Needs a small script**
- The actual field is `doc_title` (no trailing underscore, unlike the draft above - please double check the repo hasn't changed since). It repeats on every sentence rather than marking a document boundary, so deriving `# document_id` from it and hoisting `sound_url` needs two steps, run in this order:
  1. `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-document-id-from-field DIR --key doc_title --write` — dry-run against the real `.conllu` confirms this cleanly derives 5 `document_id`s.
  2. `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write` — dry-run confirms `sound_url` is constant within each of the 5 derived documents (2 distinct URLs total), so it hoists cleanly with no conflicts.
  3. Leftover per-sentence `# doc_title = ...` lines become redundant once `document_id` exists and should be deleted (a plain `grep -v '^# doc_title = '` pass, or extend the script with a `--drop-original` flag).

**Needs manual input from maintainers**
- `media` (doc-level, value seen: `spoken`) - please confirm this isn't a preliminary/partial modality tag that should instead become the standard `# modality` field once the "spoken portion identifiable" convention is settled elsewhere.
- `text_p` and `p_text` - unclear and possibly a typo/duplicate of one another; please clarify what each represents before any rename is proposed.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
