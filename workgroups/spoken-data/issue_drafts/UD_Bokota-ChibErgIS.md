---
layout: base
title: 'Issue draft: Bokota ChibErgIS'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Bokota ChibErgIS](../treebanks/UD_Bokota-ChibErgIS.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Bokota-ChibErgIS](https://github.com/UniversalDependencies/UD_Bokota-ChibErgIS)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Bokota-ChibErgIS`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field | Suggestion |
|---|---|
| — | no `newdoc id` exists at all (0 occurrences across 406 sentences) - but the 54 distinct `sound_url` values (e.g. `SAB-TXT-AN-00000-01.WAV`) already identify document boundaries; could `# newdoc id` be derived from the recording basename and set once per document? |
| `sound_url` | currently repeated on every sentence - move to document level once `newdoc id` exists |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `text_ortho` | rename to `text_orthographic` |
| `morphemic_text` | rename to `text_morphemic` |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field | Suggestion |
|---|---|
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd` | rename to `WordAlignmentEnd` |

### Implementation notes

**Quick search & replace**
- `text_ortho` → `text_orthographic`
- `morphemic_text` → `text_morphemic`
- `AlignBegin` → `WordAlignmentBegin`, `AlignEnd` → `WordAlignmentEnd` (MISC keys)
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR \
      --map text_ortho=text_orthographic,morphemic_text=text_morphemic --write
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR \
      --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write
  ```

**Needs a small script**
- Derive `# newdoc id` from `sound_url` (confirmed by dry-run: 54 distinct recordings, e.g. `SAB-TXT-AN-00000-01.WAV`), then hoist `sound_url` to document level:
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc-from-field DIR \
      --key sound_url --strip-suffix .WAV --write
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write
  ```
  Caveat: `sound_url` is a full URL (e.g. `https://corporan.huma-num.fr/Archives/media/SAB-TXT-AN-00000-01.WAV/WAV/SAB-TXT-AN-00000-01.WAV`), so the derived `newdoc id` would be the whole URL minus `.WAV`, not a clean basename - confirm the desired id format with maintainers first.
- `sent_timecode` splits cleanly into two comma-space-separated millisecond values in this treebank (dry-run against the real clone found no malformed values):
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py split-field DIR \
      --key sent_timecode --sep ', ' --into sound_alignment_begin,sound_alignment_end --write
  ```
  `duration` isn't stored and needs a follow-up computed field (`end - begin`).

**Needs manual input from maintainers**
- Confirm the newdoc-id basename format before running the derive/hoist scripts for real.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
