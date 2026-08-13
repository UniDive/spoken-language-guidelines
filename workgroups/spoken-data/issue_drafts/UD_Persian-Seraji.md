---
layout: base
title: 'Issue draft: Persian Seraji'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Persian Seraji](../treebanks/UD_Persian-Seraji.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Persian-Seraji](https://github.com/UniversalDependencies/UD_Persian-Seraji)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Persian-Seraji`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank's `genre` metadata lists `spoken` alongside `news`, `fiction`, `medical`, `legal`, `social`, `nonfiction`, but its README only mentions written data, and its `.conllu` files don't explicitly mark which sentences are spoken.

**Finding:** No genre-like field or `newdoc id` found at all, and no comment-level metadata beyond `sent_id`/`text` detected.

**Suggestion:** Could you confirm whether any part of this corpus is actually spoken, and if so, point us to which sentences/documents? Otherwise, please consider dropping `spoken` from the `genre` metadata.

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion                                                                         |
| ---------- | ---------------------------------------------------------------------------------- |
| `translit` | corpus-specific (sentence-level) - verify against metadata.html                    |
| `text_en`  | rename to `text_eng` (ISO 639-3) |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
