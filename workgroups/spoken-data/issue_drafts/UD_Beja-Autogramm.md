---
layout: base
title: 'Issue draft: Beja Autogramm'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Beja Autogramm](../treebanks/UD_Beja-Autogramm.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Beja-Autogramm](https://github.com/UniversalDependencies/UD_Beja-Autogramm)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Beja-Autogramm`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field | Suggestion |
|---|---|
| — | no `document_id` exists at all (0 occurrences across 763 sentences) - but the 18 distinct `sound_url` values (one per recording, e.g. `BEJ_MV_NARR_01_SHELTER.WAV`) already identify document boundaries; could `# document_id` be derived from the recording basename and set once per document? |
| `sound_url` | currently repeated on every sentence - move to document level once `document_id` exists |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `text_en` | rename to `text_eng` |
| `phonetic_text` | rename to `text_phonetic` |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |
| `tags` | corpus-specific (sentence-level), mostly `?`/`TO CHECK`/`TODO` placeholder values - please confirm what this represents |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field | Suggestion |
|---|---|
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd` | rename to `WordAlignmentEnd` |

### Implementation notes

**Quick search & replace**
- `text_en` → `text_eng`
- `phonetic_text` → `text_phonetic`
- `AlignBegin` → `WordAlignmentBegin`, `AlignEnd` → `WordAlignmentEnd` (MISC keys)
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR \
      --map text_en=text_eng,phonetic_text=text_phonetic --write
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR \
      --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write
  ```

**Needs a small script**
- Derive `# document_id` from `sound_url` (confirmed by dry-run: 18 distinct recordings, e.g. `BEJ_MV_NARR_01_SHELTER.WAV`), then hoist `sound_url` to document level:
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-document-id-from-field DIR \
      --key sound_url --strip-suffix .WAV --write
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write
  ```
  Caveat: `sound_url` is a full URL (e.g. `https://corporan.huma-num.fr/.../BEJ_MV_NARR_01_SHELTER.WAV`), so the derived `document_id` would be the whole URL minus `.WAV`, not a clean basename like `BEJ_MV_NARR_01_SHELTER` - confirm the desired id format with maintainers before running with `--write` (or extract the basename with a one-line regex tweak first).
- `sent_timecode` mostly holds two comma-separated millisecond values (e.g. `0, 1025`), but the separator isn't consistent (`2412,3794` with no space) and dry-running `split-field --sep ', '` against the real clone found at least one malformed value (`100298, 104357 104357, 113282` - looks like two timecodes concatenated). `duration` isn't stored and needs a computed field (`end - begin`), not a split. Recommended sequence: normalize the separator first (simple regex, e.g. `sed -E 's/([0-9]),([0-9])/\1, \2/'` on the comment lines), spot-check/fix the malformed value(s) by hand, then:
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py split-field DIR \
      --key sent_timecode --sep ', ' --into sound_alignment_begin,sound_alignment_end --write
  ```
  followed by a short script to add `duration = sound_alignment_end - sound_alignment_begin`.

**Needs manual input from maintainers**
- What `tags` represents (mostly `?`/`TO CHECK`/`TODO` placeholders) - no mechanical action possible until clarified.
- Confirm the document_id basename format above before running the script for real.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
