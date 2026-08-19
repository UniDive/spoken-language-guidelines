---
layout: base
title: 'Issue draft: English CHILDES'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to English CHILDES](../treebanks/UD_English-CHILDES.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_English-CHILDES](https://github.com/UniversalDependencies/UD_English-CHILDES)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_English-CHILDES`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

The sentences appear to be shuffled: consecutive sentences jump between corpora at random (`Brown, Brown, Braunwald, Brown, Providence, ...`). We confirmed this is real by sorting by `original_sent_id` within each `corpus_name` - that recovers a coherent original order and a constant `child_age`, so it's not just a split artifact.

| Field | Suggestion |
|---|---|
| `corpus_name` | recompose: sort sentences by `original_sent_id` within each `corpus_name`, then set `corpus_name` once per document as `# document_id` |

**Please confirm:** `corpus_name` is the CHILDES *study* name, not a single recording - e.g. `Brown` alone contains three different children (`Adam`, `Eve`, `Sarah`), and `Providence` contains three more (`Lily`, `Naima`, `Violet`). If a "document" should mean one recording session rather than an entire multi-year study, `document_id` may need to key on `(corpus_name, child_name, child_age)` instead - `child_age` looks constant within each original session.

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| `child_name` | rename to `speaker_id` |
| `child_age` | rename to `speaker_age` |
| `child_gender` | rename to `speaker_gender` |
| `chi l d` | this looks like a data bug rather than a real field: a single malformed line (`# chi l d = 37.29...`, 1 occurrence out of 48183 sentences) - almost certainly a corrupted `child_age` entry, could you check/fix the source export? |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `s_24_sent_id` | present on ~27% of sentences (12984/48183); the literal `24` looks like an unsubstituted template value - could you clarify what this represents? |

### Implementation notes

- **Quick search & replace:** `child_name`→`speaker_id`, `child_age`→`speaker_age`, `child_gender`→`speaker_gender`. Once confirmed: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map child_name=speaker_id,child_age=speaker_age,child_gender=speaker_gender --write`.
- **Needs a small (bespoke) script:** recomposing `# document_id` from `corpus_name` requires sorting sentences by `original_sent_id` within each `corpus_name` group and re-emitting the file in that order (not a mechanical rename/split - `harmonize_metadata.py` doesn't reorder sentences). A ~20-line script reading the file, grouping by `corpus_name`, sorting each group by `original_sent_id`, and rewriting with one `# document_id = <corpus_name>` per group would do it - but see the manual item below first, since the grouping key may need to change.
- **Needs manual input from maintainers:**
  - Whether "document" should mean the whole `corpus_name` study (current proposal) or one `(corpus_name, child_name, child_age)` recording session - this decides the grouping key for the recompose script above, so it should be resolved before writing it.
  - The single corrupted `# chi l d = 37.29...` line (1/48183 sentences, `en_childes-ud-train.conllu`) - looks like a broken `child_age` export; needs a source-side check/regeneration rather than a guessed fix on our end.
  - The `s_24_sent_id` field (~27% of sentences) - unclear what it represents; can't classify or script anything until clarified.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
