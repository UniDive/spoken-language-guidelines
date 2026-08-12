---
layout: base
title: 'Issue draft: Komi_Zyrian IKDP'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Komi_Zyrian IKDP](../treebanks/UD_Komi_Zyrian-IKDP.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Komi_Zyrian-IKDP](https://github.com/UniversalDependencies/UD_Komi_Zyrian-IKDP)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Komi_Zyrian-IKDP`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but per the README, `sent_id` values match those in the archived IKDP corpus, with `+` marking sentence IDs that span multiple annotations (a merge within one recording, not a document boundary). This suggests `sent_id` already encodes a document/recording identifier.

| Field | Suggestion                                                                                                                                                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` prefix identifying the source recording (please confirm the exact delimiter); treat `+`-joined `sent_id`s as belonging to the same document |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion         |
| ---------- | ------------------ |
| `text_en`  | make tags: text_en |
| `text_ru`  | text_rus           |
| `text_end` | text_en            |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field      | Suggestion           |
| ---------- | -------------------- |
| `OrigLang` | rename to `OrigLang` |
| `Lang`     | rename to `Lang`     |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
