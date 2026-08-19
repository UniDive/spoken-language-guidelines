---
layout: base
title: 'Issue draft: Yiddish YiTB'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Yiddish YiTB](../treebanks/UD_Yiddish-YiTB.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Yiddish-YiTB](https://github.com/UniversalDependencies/UD_Yiddish-YiTB)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Yiddish-YiTB`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (fairly confident):

**Finding:** Identifiable via the sentence-level `genre` field, which has two spoken-tagged values.

**Evidence:** `genre` (9 distinct values): `grammar-examples/learner-essays` (2,437), `spoken, web` (160), `nonfiction` (126), `bible` (126), `fiction` (120), `proverb` (60), `wiki` (19), `spoken, liturgical` (5), `grammar-examples` (1). 165 sentences have a `genre` value containing "spoken".

**Suggestion:** Add `# modality = spoken` to the 165 sentences whose `genre` value contains "spoken" (`spoken, web` / `spoken, liturgical`).

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field    | Suggestion                                                               |
| -------- | ------------------------------------------------------------------------ |
| `rtl`    | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `source` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion                                                      |
| ---------- | --------------------------------------------------------------- |
| `translit` | rename to `text_translitteration`                               |
| `text_en`  | rename to `text_eng` (ISO 639-3)                                |
| `note`     | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

- **Quick search & replace:**
  - `translit` → `text_translitteration`, `text_en` → `text_eng`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment UD_Yiddish-YiTB --map translit=text_translitteration,text_en=text_eng --write`.
- **Needs a small script:** add `# modality = spoken` to the 165 sentences whose sentence-level `genre` contains "spoken" (`spoken, web` / `spoken, liturgical` - confirmed present, e.g. in `yi_yitb-ud-train.conllu`). This is sentence-level, not doc-level, so `harmonize_metadata.py tag-modality` (which keys off `document_id`) doesn't apply directly - needs a short variant:
  ```python
  # for each `# genre = ...` comment containing "spoken", insert
  # `# modality = spoken` right after it
  ```
  or equivalently `sed -i '' '/^# genre = .*spoken/a\
# modality = spoken' *.conllu`.
- **Needs manual input from maintainers:** `rtl` and `source` (speaker/paragraph-level, corpus-specific) and `note` (sentence-level) all need a naming decision against the conventions.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
