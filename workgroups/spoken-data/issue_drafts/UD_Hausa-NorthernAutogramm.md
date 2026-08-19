---
layout: base
title: 'Issue draft: Hausa NorthernAutogramm'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Hausa NorthernAutogramm](../treebanks/UD_Hausa-NorthernAutogramm.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Hausa-NorthernAutogramm](https://github.com/UniversalDependencies/UD_Hausa-NorthernAutogramm)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Hausa-NorthernAutogramm`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field           | Suggestion                                                                |
| --------------- | ------------------------------------------------------------------------- |
| `text_en`       | change to `text_eng`                                                      |
| `text_ortho`    | change to `text_orthographic`                                             |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |
| `sound_url`     | possibly move to document level                                           |

### 2. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### Implementation notes

- **Quick search & replace:** `text_en`→`text_eng`, `text_ortho`→`text_orthographic`, `AlignBegin`→`WordAlignmentBegin`, `AlignEnd`→`WordAlignmentEnd`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map text_en=text_eng,text_ortho=text_orthographic --write` and `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`.
- **Needs a small script:**
  - Splitting `sent_timecode` (verified format `"3540, 8040"`, i.e. `"<begin>, <end>"` in ms) into begin/end: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py split-field DIR --key sent_timecode --sep ', ' --into sound_alignment_begin,sound_alignment_end --write`. `duration` isn't a plain split - it needs a follow-up computation (`end - begin`); a short (~10-line) script pass after the split would add it.
  - Moving `sound_url` to document level: `document_id` already exists here, so `hoist-to-doc` can run directly. Dry-run against `ha_northernautogramm-ud-test.conllu` (+ `not-to-release/original_split/`): 7 documents hoist cleanly, 1 is flagged NOT constant (multiple `sound_url` values in the same document) - flag that one to maintainers before running `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write` for real.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
