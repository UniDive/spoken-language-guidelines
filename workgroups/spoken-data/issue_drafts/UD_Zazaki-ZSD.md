---
layout: base
title: 'Issue draft: Zazaki ZSD'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Zazaki ZSD](../treebanks/UD_Zazaki-ZSD.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Zazaki-ZSD](https://github.com/UniversalDependencies/UD_Zazaki-ZSD)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Zazaki-ZSD`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `document_id` exists, but it's trivial to derive: `sent_id` follows `Seyristane_dialogue_<number><A/B>` (e.g. `Seyristane_dialogue_171A`), and the whole corpus (200 sentences) is a single interview/dialogue.

| Field | Suggestion                                                            |
| ----- | --------------------------------------------------------------------- |
| —     | add `# document_id = Seyristane_dialogue` corpus-wide (single document) |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field     | Suggestion                       |
| --------- | -------------------------------- |
| `text_en` | rename to `text_eng` (ISO 639-3) |

### Implementation notes

- **Quick search & replace:** `text_en` → `text_eng`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment UD_Zazaki-ZSD --map text_en=text_eng --write`.
- **Needs a small script:** add `# document_id = Seyristane_dialogue` corpus-wide.
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-document-id \
      UD_Zazaki-ZSD --pattern '^(?P<doc>Seyristane_dialogue)_\d+[AB](?:_split\d+)?$' --write
  ```
  Verified against the local clone (dry-run, all three splits): the simpler pattern from the issue draft (`^(?P<doc>.+)-\d+$`-style, without the `_split\d+` suffix) misses 2 `sent_id`s in the test split (`Seyristane_dialogue_185A_split1`/`_split2`) - the pattern above (with the optional `_split\d+` suffix) correctly derives the single document across all three files with no unmatched `sent_id`s.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
