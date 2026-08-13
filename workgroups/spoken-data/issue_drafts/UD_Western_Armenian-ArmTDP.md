---
layout: base
title: 'Issue draft: Western_Armenian ArmTDP'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Western_Armenian ArmTDP](../treebanks/UD_Western_Armenian-ArmTDP.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Western_Armenian-ArmTDP](https://github.com/UniversalDependencies/UD_Western_Armenian-ArmTDP)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Western_Armenian-ArmTDP`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (fairly confident):

**Finding:** Identifiable via the `newdoc id` prefix, which already encodes genre.

**Evidence:** `newdoc id` values are `genre-code`, e.g. `spoken-002R`. Full prefix distribution: news (38), fiction (16), blog (15), nonfiction (9), wiki (7), reviews (3), web (2), spoken (2), social (1).

**Suggestion:** Add `# modality = spoken` to the 2 documents whose `newdoc id` starts with `spoken-`.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                                                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `doc_title` | `newdoc id` already exists separately (e.g. `spoken-002R`); `doc_title` is the human-readable document title - keep as corpus-specific |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion                                                      |
| ---------- | --------------------------------------------------------------- |
| `translit` | corpus-specific (sentence-level) - verify against metadata.html |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
