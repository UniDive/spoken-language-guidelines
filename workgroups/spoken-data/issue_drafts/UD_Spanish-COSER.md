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

### Implementation notes

- **Needs manual input from maintainers:** the document/recording structure question (item 1) - whether `orig_turn_id`'s numeric prefix corresponds to one recording, and how to resolve the one prefix (`3203`) that spans 36 `location` values. This has to be settled before any document-level `document_id` can be derived.
- **Needs a small script:** `turn_time` and `time` aren't simple field renames - they need format parsing (verified in the local clone: `turn_time` values look like `01:25:28.640000-01:26:47.121270` or `01:17:53.37-01:18:00.72`, `time` uses `HH:MM:SS,mmm--> HH:MM:SS,mmm`), conversion to milliseconds, splitting into `sound_alignment_begin`/`sound_alignment_end`, and deriving `duration` as their difference. This isn't covered by `workgroups/spoken-data/scripts/harmonize_metadata.py`'s generic `split-field` (which does a plain separator split, not a time-parse + unit conversion + derived field) - it needs a small bespoke script, e.g.:
  ```python
  import re
  def to_ms(hms):
      h, m, s = re.split('[:,]', hms.replace('-->', ':'))[:3]
      return (int(h)*3600 + int(m)*60 + float(s.replace(',', '.'))) * 1000
  # for each `# turn_time = A-B` or `# time = A--> B` comment:
  #   begin, end = to_ms(A), to_ms(B)
  #   emit sound_alignment_begin=begin, sound_alignment_end=end, duration=end-begin
  ```
  Best deferred until the document-structure question above is resolved, since it may affect where `duration` ends up living.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
