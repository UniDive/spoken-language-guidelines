---
layout: base
title: 'Issue draft: Cantonese HK'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Cantonese HK](../treebanks/UD_Cantonese-HK.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Cantonese-HK](https://github.com/UniversalDependencies/UD_Cantonese-HK)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Cantonese-HK`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists in the current `.conllu` (the field this section previously listed, `_filename`, is not actually present - that suggestion was stale). However, the repo's own README documents exactly 4 distinct sources by `sent_id` range, each with a title, source URL, and fluency note:

| `sent_id` range | Title | Fluency |
|---|---|---|
| 1-410 | Missing days / 小時光 (film) | mostly prepared dialogue |
| 411-547 | Tempo in Temple / 廟眾樂樂 (film) | spontaneous interview |
| 548-650 | What day is today / 今日星期幾 (film) | mostly prepared |
| 651-1004 | Legislative Council meeting (2016-10-12) | spontaneous discussion |

| Field | Suggestion |
|---|---|
| — | add `# newdoc id` at sentences 1, 411, 548, and 651 (one per source above) |
| — | add `# genre` (film / legislative-proceedings) and `degree_of_spontaneity` (`planned` for the 3 films, `unplanned` for the legislative discussion and the "Tempo in Temple" interview) per document |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| — | no speaker metadata exists; the legislative-council portion (sentences 651-1004) clearly involves multiple speakers - could `speaker_id` be recovered and tagged? |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
