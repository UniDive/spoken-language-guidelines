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

| `sent_id` range | Proposed `newdoc id` | Title | Fluency |
|---|---|---|---|
| 1-410 | `missing_days` | Missing days / 小時光 (film) | mostly prepared dialogue |
| 411-547 | `tempo_in_temple` | Tempo in Temple / 廟眾樂樂 (film) | spontaneous interview |
| 548-650 | `what_day_is_today` | What day is today / 今日星期幾 (film) | mostly prepared |
| 651-1004 | `legco_president_election_2016` | Legislative Council meeting (2016-10-12) | spontaneous discussion |

| Field | Suggestion |
|---|---|
| — | add `# newdoc id` at sentences 1, 411, 548, and 651, using the proposed ids above (please confirm the slugs) |
| — | add `# genre` (film / legislative-proceedings) and `degree_of_spontaneity` (`planned` for the 3 films, `unplanned` for the legislative discussion and the "Tempo in Temple" interview) per document |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| — | no speaker metadata exists; the legislative-council portion (sentences 651-1004) clearly involves multiple speakers - could `speaker_id` be recovered and tagged? |

### Implementation notes

**Quick search & replace**
- None.

**Needs a small script**
- `sent_id` is a plain sequential integer (`1`, `2`, ... `1004`, confirmed by dry inspection of the clone) with no separator to derive document boundaries from - `harmonize_metadata.py derive-newdoc` doesn't apply here since it needs a regex-extractable prefix. Instead, insert `# newdoc id` (and `# genre`/`# degree_of_spontaneity`) at the four fixed `sent_id` boundaries (1, 411, 548, 651) with a short bespoke script (~15 lines: iterate sentences, insert a comment block when `sent_id` matches one of the four boundary values). Happy to write this once the id slugs and genre/spontaneity values are confirmed.

**Needs manual input from maintainers**
- Confirm the four proposed `newdoc id` slugs (`missing_days`, `tempo_in_temple`, `what_day_is_today`, `legco_president_election_2016`).
- Confirm `genre` and `degree_of_spontaneity` values per document.
- Whether `speaker_id` can be recovered for the legislative-council portion (sentences 651-1004) - needs source material, not a mechanical transform.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
