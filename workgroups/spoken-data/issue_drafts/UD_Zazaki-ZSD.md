---
layout: base
title: 'Issue draft: Zazaki ZSD'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Zazaki ZSD](../treebanks/UD_Zazaki-ZSD.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Zazaki-ZSD](https://github.com/UniversalDependencies/UD_Zazaki-ZSD)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Zazaki-ZSD`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but it's trivial to derive: `sent_id` follows `Seyristane_dialogue_<number><A/B>` (e.g. `Seyristane_dialogue_171A`), and the whole corpus (200 sentences) is a single interview/dialogue.

| Field | Suggestion                                                            |
| ----- | --------------------------------------------------------------------- |
| —     | add `# newdoc id = Seyristane_dialogue` corpus-wide (single document) |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field     | Suggestion                       |
| --------- | -------------------------------- |
| `text_en` | rename to `text_eng` (ISO 639-3) |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
