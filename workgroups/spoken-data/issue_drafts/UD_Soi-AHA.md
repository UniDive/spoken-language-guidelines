---
layout: base
title: 'Issue draft: Soi AHA'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Soi AHA](../treebanks/UD_Soi-AHA.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Soi-AHA](https://github.com/UniversalDependencies/UD_Soi-AHA)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Soi-AHA`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

The README states the treebank "is based on interviews with Soi speakers"; despite `genre` listing `grammar-examples spoken`, the whole corpus (8 sentences) is spoken.

**Suggestion:** Add `# modality = spoken` corpus-wide.

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field     | Suggestion                       |
| --------- | -------------------------------- |
| `text_en` | change to `text_eng` (ISO 639-3) |
| `text_fa` | change to `text_fas` (ISO 639-3) |

### Implementation notes

**Quick search & replace**
- `text_en` → `text_eng`, `text_fa` → `text_fas`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map text_en=text_eng,text_fa=text_fas --write`
- `# modality = spoken` corpus-wide (only 8 sentences, single small file): a one-line loop is simpler than a script - `sed -i '' '/^# sent_id/i\
# modality = spoken' DIR/*.conllu` (insert once before every `# sent_id`), or equivalently `rename-comment`/`tag-modality` don't apply since there's no existing field to key off - this is just inserting a constant comment everywhere.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
