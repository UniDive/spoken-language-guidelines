---
layout: base
title: 'Issue draft: Spanish COSER'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Spanish COSER](../treebanks/UD_Spanish-COSER.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Spanish-COSER](https://github.com/UniversalDependencies/UD_Spanish-COSER)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Spanish-COSER`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

The organization into documents is not clear from the data. Sentences come from two merged sources with different `sent_id` schemes: 474 use a dialect-region prefix (`anda-230`, `arag-...`, etc. - 17 distinct regions, too coarse to be a document) plus `orig_turn_id` (`<4-digit-id>-<turn>`, e.g. `1823-0229`); the other 65 use an ALEC-style `sent_id` (`ALEC_C11_Bo46_2`) with a `time` field instead of `turn_time`/`orig_turn_id`. The `orig_turn_id` prefix maps 1:1 to `location` in almost all cases, but one prefix (`3203`) spans 36 different locations, which breaks a clean derivation.

**Suggestion:** Could you clarify the intended document/recording structure (e.g. does `orig_turn_id`'s prefix correspond to one recording/interview)?

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

`turn_time` (`HH:MM:SS[.ffffff]-HH:MM:SS[.ffffff]`, 474 sentences) and `time` (`HH:MM:SS,mmm--> HH:MM:SS,mmm`, 65 ALEC-sourced sentences) both encode a begin-end range for the same purpose, just with different formats/precision. Both should convert to milliseconds and split into the standard timing fields.

| Field       | Suggestion                                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `turn_time` | convert to milliseconds, split into `sound_alignment_begin` and `sound_alignment_end`; derive `duration`                             |
| `time`      | convert to milliseconds, split into `sound_alignment_begin` and `sound_alignment_end` (same as `turn_time`, different format/source) |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
