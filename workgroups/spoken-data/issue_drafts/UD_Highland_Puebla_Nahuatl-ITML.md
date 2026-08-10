---
layout: base
title: 'Issue draft: Highland_Puebla_Nahuatl ITML'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Highland_Puebla_Nahuatl ITML](../treebanks/UD_Highland_Puebla_Nahuatl-ITML.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Highland_Puebla_Nahuatl-ITML](https://github.com/UniversalDependencies/UD_Highland_Puebla_Nahuatl-ITML)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Highland_Puebla_Nahuatl-ITML`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken.

**Finding:** Identifiable via `sent_id`: sentences from spoken material carry a `.eaf` (ELAN annotation file) reference in their `sent_id`.

**Suggestion:** Add `# modality = spoken` to sentences whose `sent_id` contains `.eaf`.

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field         | Suggestion                                                      |
| ------------- | --------------------------------------------------------------- |
| `text[spa]`   | make tags: text_sp                                              |
| `text[orig]`  | transl_LANGUAGE                                                 |
| `text[gloss]` | make tags: text_gloss                                           |
| `text[glosa]` | corpus-specific (sentence-level) - verify against metadata.html |
| `text[a140]`  | corpus-specific (sentence-level) - verify against metadata.html |

### 3. Other / corpus-specific

| Field    | Suggestion |
| -------- | ---------- |
| `labels` | revise     |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
