---
layout: base
title: 'Issue draft: Turkish_German SAGT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Turkish_German SAGT](../treebanks/UD_Turkish_German-SAGT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Turkish_German-SAGT](https://github.com/UniversalDependencies/UD_Turkish_German-SAGT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Turkish_German-SAGT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but it can be derived directly from the `sent_id` prefix: `sent_id` follows `<doc-id>-<number>` (e.g. `TRDE-CS-C15-0001`), with 48 distinct document ids (`TRDE-CS-C01` ... `TRDE-CS-V06`).

| Field | Suggestion                                                                                  |
| ----- | ------------------------------------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` prefix (everything before the trailing `-<number>`) |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field                     | Suggestion                                                      |
| ------------------------- | --------------------------------------------------------------- |
| `NOTE`                    | corpus-specific (sentence-level) - verify against metadata.html |
| `annotated with partaxis` | corpus-specific (sentence-level) - verify against metadata.html |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field  | Suggestion       |
| ------ | ---------------- |
| `Lang` | rename to `Lang` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
