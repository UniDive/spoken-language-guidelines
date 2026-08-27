---
layout: base
title: 'Issue draft: Hausa SouthernAutogramm'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Hausa SouthernAutogramm](../treebanks/UD_Hausa-SouthernAutogramm.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Hausa-SouthernAutogramm](https://github.com/UniversalDependencies/UD_Hausa-SouthernAutogramm)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Hausa-SouthernAutogramm`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                      |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field           | Suggestion                                                                |
| --------------- | ------------------------------------------------------------------------- |
| `text_en`       | OK (ISO 639-1 two-letter code)                                     |
| `phonetic_text` | change to `text_phonetic`                                                 |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |
| `Lang`       | rename to `Lang`               |

### Implementation notes

- **Quick search & replace:** `phonetic_text`→`text_phonetic`, `AlignBegin`→`WordAlignmentBegin`, `AlignEnd`→`WordAlignmentEnd`, `Lang`→`Lang` (already standard, no action needed): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map phonetic_text=text_phonetic --write` and `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`.
- **Needs a small script:**
  - Splitting `sent_timecode` into begin/end (same `"<begin>, <end>"` format as Hausa-NorthernAutogramm, verified against `ha_southernautogramm-ud-test.conllu`): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py split-field DIR --key sent_timecode --sep ', ' --into sound_alignment_begin,sound_alignment_end --write`; `duration` needs a small follow-up computation (`end - begin`), not a plain split.
  - Moving `sound_url` to document level: `document_id` already exists here. Dry-run against `ha_southernautogramm-ud-test.conllu` (+ `not-to-release/original_split/`): 8 documents hoist cleanly, 1 flagged NOT constant - flag that one before running `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write` for real. (Note: the draft only lists this at document level as "possibly move" - worth confirming it should apply the same way as the Northern variant.)

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
