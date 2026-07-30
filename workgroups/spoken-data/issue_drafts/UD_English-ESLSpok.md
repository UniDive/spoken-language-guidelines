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

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
