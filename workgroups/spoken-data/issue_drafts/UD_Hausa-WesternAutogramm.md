---
layout: base
title: 'Issue draft: Hausa WesternAutogramm'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Hausa WesternAutogramm](../treebanks/UD_Hausa-WesternAutogramm.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Hausa-WesternAutogramm](https://github.com/UniversalDependencies/UD_Hausa-WesternAutogramm)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Hausa-WesternAutogramm`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (no signal found):

**Finding:** No genre-like field or `newdoc id` found at all.

**Evidence:** No comment-level metadata beyond `sent_id`/`text` detected.

**Suggestion:** Could you point us to which sentences/documents are spoken vs. written?

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                      |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field        | Suggestion |
| ------------ | ---------- |
| `speaker_id` | OK         |

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field           | Suggestion                                                                |
| --------------- | ------------------------------------------------------------------------- |
| `text_en`       | change to `text_eng`                                                      |
| `text_ortho`    | change to `text_orthographic`                                             |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
