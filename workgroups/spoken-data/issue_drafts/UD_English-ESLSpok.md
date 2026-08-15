---
layout: base
title: 'Issue draft: English ESLSpok'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to English ESLSpok](../treebanks/UD_English-ESLSpok.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_English-ESLSpok](https://github.com/UniversalDependencies/UD_English-ESLSpok)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_English-ESLSpok`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but `sent_id` already encodes document structure: e.g. `file01243.txt_145` is document `file01243.txt`, sentence `145`. 872 distinct documents across 2320 sentences (up to 22 sentences per document). Like CHILDES, the sentences are shuffled - consecutive sentences jump between documents at random. Per the README, this is "a random sample of sentences" from a spoken L2 English interview corpus, so each document is one interview session, only partially sampled here.

| Field | Suggestion |
|---|---|
| — | derive `# newdoc id` from the `sent_id` prefix (before `_<number>`); recompose by sorting within each prefix by that trailing number |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| — | no speaker metadata exists; each document is one L2 English speaker's interview session - could `speaker_id` be derived from the same filename once `newdoc id` is introduced? |

### Implementation notes

- **Needs a small script:** deriving `# newdoc id` from the `sent_id` prefix is mechanical and verified clean (0 sent_ids fail to match, run against all three release files): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc DIR --pattern '^(?P<doc>.+)_\d+$' --write` (dry-run against `en_eslspok-ud-{dev,test,train}.conllu` derives 198/200/808 doc ids respectively - the 872 distinct-document figure in the draft is the union across all three splits, since a document's sentences can be split across dev/train/test, so the count is correctly done per-file). This only inserts the id; it does **not** recompose sentence order (see manual item below).
- **Needs manual input from maintainers:** recomposing "shuffled" sentences into their original per-document order needs the true source ordering key, which isn't in the current fields (unlike CHILDES, there's no visible `original_sent_id` equivalent here) - could you point us to what determines original order, or confirm the corpus should stay as one-sentence-per-doc-order-unknown? Same for `speaker_id`: whether it can simply be derived from the (soon-to-exist) `newdoc id` needs a maintainer confirmation before scripting it (trivial `rename-comment`-style copy once confirmed).

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
