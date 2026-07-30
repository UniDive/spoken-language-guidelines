---
layout: base
title: 'Issue draft: Chukchi HSE'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Chukchi HSE](../treebanks/UD_Chukchi-HSE.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Chukchi-HSE](https://github.com/UniversalDependencies/UD_Chukchi-HSE)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Chukchi-HSE`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `# newdoc id` exists, but document boundaries are fully recoverable: per the README, `sent_id` encodes `<filename>:<sentence_number>`, where `<filename>` matches the text's name on the source corpus site ([chuklang.ru](http://chuklang.ru/)). Splitting `sent_id` on `:` gives 65 distinct documents across the 1004 sentences.

| Field | Suggestion |
|---|---|
| — | derive `# newdoc id` from the `sent_id` prefix (everything before `:`), set once at each document's first sentence |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `text[eng]` | rename to `text_eng` |
| `text[eng']` | rename to `text_eng_literal` |
| `text[rus]` | rename to `text_rus` |
| `text[phon]` | rename to `text_phonetic` |
| `timestamp` | change to `sound_alignment_begin`, `sound_alignment_end` and `duration` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
