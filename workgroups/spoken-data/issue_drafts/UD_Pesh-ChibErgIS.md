---
layout: base
title: 'Issue draft: Pesh ChibErgIS'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Pesh ChibErgIS](../treebanks/UD_Pesh-ChibErgIS.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Pesh-ChibErgIS](https://github.com/UniversalDependencies/UD_Pesh-ChibErgIS)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Pesh-ChibErgIS`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but it can be derived from the `sent_id` prefix (please confirm the exact delimiter/recording identifier).

| Field       | Suggestion                                                                      |
| ----------- | ------------------------------------------------------------------------------- |
| —           | derive `# newdoc id` from the `sent_id` prefix identifying the source recording |
| `sound_url` | move to document level                                                          |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field                 | Suggestion                                                                |
| --------------------- | ------------------------------------------------------------------------- |
| `text_phrase-gls-es`  | make tags text_sp                                                         |
| `text_phrase-gls-tl`  | text_tl                                                                   |
| `text_phrase-gls-de`  | text_de                                                                   |
| `morphemic_text`      | make tags: annot_morph                                                    |
| `text_phrase-gls-it`  | text_phon                                                                 |
| `text_phrase-gls-pro` | annot_prosodic                                                            |
| `text_phrase-gls-wg`  | text_gloss                                                                |
| `sent_timecode`       | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
