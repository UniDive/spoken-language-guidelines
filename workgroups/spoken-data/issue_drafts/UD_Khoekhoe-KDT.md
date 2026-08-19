---
layout: base
title: 'Issue draft: Khoekhoe KDT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Khoekhoe KDT](../treebanks/UD_Khoekhoe-KDT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Khoekhoe-KDT](https://github.com/UniversalDependencies/UD_Khoekhoe-KDT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Khoekhoe-KDT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (a reasonable guess):

**Finding:** Likely identifiable via the `document_id` prefix, which names the source type.

**Evidence:** `document_id` prefixes (small, clean set): `book` (15), `grammar` (2), `film` (2), `conversation` (1). `conversation` and `film` (transcribed dialogue/subtitles) are plausibly spoken; `book`/`grammar` are written.

**Suggestion:** Add `# modality = spoken` to documents whose `document_id` starts with `conversation` or `film` - please confirm whether `film` here means subtitle/transcript text.

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

### Implementation notes

**Quick search & replace**
- `english` → `text_eng` (`# english =` → `# text_eng =`).
- `OrigLang`, `Lang`: already the standard MISC key names in the released data (verified) - no change needed, the draft's "rename to X" here is a no-op.

**Needs a small script**
- Modality tagging, once confirmed: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality <path> --spoken-if '^(conversation|film)' --written-if '^(book|grammar)' --write`. Dry-run against all three released files (`naq_kdt-ud-{dev,test,train}.conllu`) tags all 25 `document_id`s cleanly (15 book, 4 grammar → written; 3 conversation, 3 film → spoken), no unmatched ids.

**Needs manual input from maintainers**
- Whether `film` documents are subtitle/transcript text (spoken) as assumed - confirms the regex above.
- `parallel_id`: corpus-specific field, needs a decision on whether/how it maps to the naming conventions before any action.
