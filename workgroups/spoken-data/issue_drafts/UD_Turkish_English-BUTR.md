---
layout: base
title: 'Issue draft: Turkish_English BUTR'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Turkish_English BUTR](../treebanks/UD_Turkish_English-BUTR.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Turkish_English-BUTR](https://github.com/UniversalDependencies/UD_Turkish_English-BUTR)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Turkish_English-BUTR`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

`type` says `only spoken`, but the corpus is actually mixed. The README documents `# medium` as "Communication medium (Written or Spoken), where known", and in the data it's only present on 19 of 58 sentences (`Spoken` or `Written`).

**Suggestion:** Could you confirm modality for the remaining 39 sentences? In the meantime, `medium` maps directly onto our `# modality` field.

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field     | Suggestion                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------ |
| `text_en` | rename to `text_eng` (ISO 639-3)                                                                                         |
| `medium`  | rename to `# modality` (values `spoken`/`written`, lowercase); only present on 19/58 sentences - please confirm the rest |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
