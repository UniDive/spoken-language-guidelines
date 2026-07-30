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
| — | no `newdoc id` exists at all (0 occurrences across 763 sentences) - but the 18 distinct `sound_url` values (one per recording, e.g. `BEJ_MV_NARR_01_SHELTER.WAV`) already identify document boundaries; could `# newdoc id` be derived from the recording basename and set once per document? |
| `sound_url` | currently repeated on every sentence - move to document level once `newdoc id` exists |

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

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
