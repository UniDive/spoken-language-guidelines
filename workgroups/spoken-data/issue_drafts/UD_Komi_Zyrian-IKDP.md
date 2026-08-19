---
layout: base
title: 'Issue draft: Komi_Zyrian IKDP'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Komi_Zyrian IKDP](../treebanks/UD_Komi_Zyrian-IKDP.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Komi_Zyrian-IKDP](https://github.com/UniversalDependencies/UD_Komi_Zyrian-IKDP)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Komi_Zyrian-IKDP`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `document_id` exists, but per the README, `sent_id` values match those in the archived IKDP corpus, with `+` marking sentence IDs that span multiple annotations (a merge within one recording, not a document boundary). This suggests `sent_id` already encodes a document/recording identifier.

| Field | Suggestion                                                                                                                                                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| —     | derive `# document_id` from the `sent_id` prefix identifying the source recording (please confirm the exact delimiter); treat `+`-joined `sent_id`s as belonging to the same document |

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

### Implementation notes

**Quick search & replace**
- `text_ru` → `text_rus`, `text_end` → `text_en` (`text_end` looks like a typo for `text_en`; confirm before merging with any existing `text_en`). `text_en` itself is already correctly named.
- `OrigLang`, `Lang`: already the standard MISC key names (verified) - no change needed.

**Needs a small script**
- Once the `sent_id` delimiter is confirmed (see below), deriving `# document_id`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-document-id <path> --pattern '<confirmed-pattern>' --write`.

**Needs manual input from maintainers**
- `sent_id` document delimiter: two different conventions are visible in the data itself - `13756_2bz.002` (dot before a numeric suffix) and `kpv_izva19591100-05582_1az-04` (dash before the suffix) - so a single regex can't derive `document_id` for the whole corpus automatically; need the exact rule (and confirmation that a single rule covers all recordings).
- `+`-joined `sent_id`s (e.g. `kpv_izva20140325-2-a-027+...+031`, up to 5-way merges): confirmed by the draft to belong to one document, but `derive-document-id` as written takes the *first* sent_id in a merge as the document key - should double check merged-sentence handling once the delimiter rule is set.
