---
layout: base
title: 'Issue draft: Nenets Tundra'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Nenets Tundra](../treebanks/UD_Nenets-Tundra.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Nenets-Tundra](https://github.com/UniversalDependencies/UD_Nenets-Tundra)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Nenets-Tundra`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but `doc_title_` already identifies the document and can be used directly to introduce it.

| Field        | Suggestion                                                                           |
| ------------ | ------------------------------------------------------------------------------------ |
| `doc_title_` | use as `# newdoc id` (rename/repurpose the field)                                    |
| `sound_url`  | possibly rename to `sound_url` (see Document-level in metadata.html) - please verify |
| `media`      | corpus-specific (doc-level) - verify against metadata.html                           |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field              | Suggestion              |
| ------------------ | ----------------------- |
| `speaker metadata` | make tags: speaker_id   |
| `?`                | add speaker_INFORMATION |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion    |
| ---------- | ------------- |
| `text_p`   | unclear, keep |
| `translit` | text_translit |
| `p_text`   | unclear, keep |

### 4. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
