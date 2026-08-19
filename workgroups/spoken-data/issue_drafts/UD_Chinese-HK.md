---
layout: base
title: 'Issue draft: Chinese HK'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Chinese HK](../treebanks/UD_Chinese-HK.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Chinese-HK](https://github.com/UniversalDependencies/UD_Chinese-HK)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Chinese-HK`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `document_id` exists in the current `.conllu`. However, the repo's own README documents exactly 4 distinct sources by `sent_id` range (matching the parallel UD_Cantonese-HK treebank):

| `sent_id` range | Proposed `document_id` | Title | Source |
|---|---|---|---|
| 1-410 | `missing_days` | Missing days / 小時光 (film) | https://www.youtube.com/watch?v=1qSMiw0vhzU |
| 411-547 | `tempo_in_temple` | Tempo in Temple / 廟眾樂樂 (film) | https://www.youtube.com/watch?v=8e8Lqd6grTE |
| 548-650 | `what_day_is_today` | What day is today / 今日星期幾 (film) | https://www.youtube.com/watch?v=bBGwxIDiZ_o |
| 651-1004 | `legco_president_election_2016` | Legislative Council meeting (2016-10-12) | https://www.legco.gov.hk/yr16-17/chinese/counmtg/hansard/cm20161012-translate-c.pdf |

| Field | Suggestion |
|---|---|
| — | add `# document_id` at sentences 1, 411, 548, and 651, using the proposed ids above (please confirm the slugs; same ranges as the parallel UD_Cantonese-HK treebank) |
| — | add `# genre` (film / legislative-proceedings) per document |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| — | no speaker metadata exists; the legislative-council portion (sentences 651-1004) clearly involves multiple speakers - could `speaker_id` be recovered and tagged? |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `translit` | pinyin transcription (added in v2.12) - rename to `text_transliteration` |

### Implementation notes

**Quick search & replace**
- `translit` → `text_transliteration`
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map translit=text_transliteration --write
  ```

**Needs a small script**
- Same situation as the parallel UD_Cantonese-HK treebank: `sent_id` is a plain sequential integer with no derivable prefix, so `derive-document-id` doesn't apply. Insert `# document_id` (and `# genre`) at the four fixed `sent_id` boundaries (1, 411, 548, 651) with a short bespoke script, once the id slugs and genre values are confirmed - can share the same script written for UD_Cantonese-HK since the boundaries match exactly.

**Needs manual input from maintainers**
- Confirm the four proposed `document_id` slugs (same as UD_Cantonese-HK: `missing_days`, `tempo_in_temple`, `what_day_is_today`, `legco_president_election_2016`).
- Confirm `genre` values per document.
- Whether `speaker_id` can be recovered for the legislative-council portion (sentences 651-1004) - needs source material, not a mechanical transform.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
