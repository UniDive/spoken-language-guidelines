---
layout: base
title: 'Issue draft: Khoekhoe KDT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Khoekhoe KDT](../treebanks/UD_Khoekhoe-KDT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Khoekhoe-KDT](https://github.com/UniversalDependencies/UD_Khoekhoe-KDT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Khoekhoe-KDT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (a reasonable guess):

**Finding:** Likely identifiable via the `newdoc id` prefix, which names the source type.

**Evidence:** `newdoc id` prefixes (small, clean set): `book` (15), `grammar` (2), `film` (2), `conversation` (1). `conversation` and `film` (transcribed dialogue/subtitles) are plausibly spoken; `book`/`grammar` are written.

**Suggestion:** Add `# modality = spoken` to documents whose `newdoc id` starts with `conversation` or `film` - please confirm whether `film` here means subtitle/transcript text.

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field         | Suggestion                                                      |
| ------------- | --------------------------------------------------------------- |
| `english`     | change to `text_eng` (ISO 639-3) |
| `parallel_id` | corpus-specific (sentence-level) - verify against metadata.html |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field      | Suggestion           |
| ---------- | -------------------- |
| `OrigLang` | rename to `OrigLang` |
| `Lang`     | rename to `Lang`     |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
