---
layout: base
title: 'Issue draft: Italian KIParlaForest'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Italian KIParlaForest](../treebanks/UD_Italian-KIParlaForest.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Italian-KIParlaForest](https://github.com/UniversalDependencies/UD_Italian-KIParlaForest)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Italian-KIParlaForest`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field             | Suggestion        |
| ----------------- | ----------------- |
| `conversation_id` | make tags: doc_id |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field            | Suggestion              |
| ---------------- | ----------------------- |
| `jefferson_text` | make tags: text_transcr |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field   | Suggestion                     |
| ------- | ------------------------------ |
| `Begin` | rename to `WordAlignmentBegin` |
| `End`   | rename to `WordAlignmentEnd`   |

### Implementation notes

**Quick search & replace**
- `conversation_id` → `doc_id` (`# conversation_id =` → `# doc_id =`).
- `jefferson_text` → `text_transcr` (`# jefferson_text =` → `# text_transcr =`).
- `Begin` → `WordAlignmentBegin`, `End` → `WordAlignmentEnd` (token-level MISC keys):
  `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc <path> --map Begin=WordAlignmentBegin,End=WordAlignmentEnd --write`
  (verified against `it_kiparlaforest-ud-test.conllu` - both keys are present in MISC and rename cleanly.)

**Needs a small script**
- None - all three items above are straightforward renames the script above already handles; no structural change needed.

**Needs manual input from maintainers**
- None outstanding.
