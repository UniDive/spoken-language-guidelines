---
layout: base
title: 'Chinese HK'
udver: '2'
---

# Chinese HK

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.1 |
| **link** | [https://github.com/UniversalDependencies/UD_Chinese-HK](https://github.com/UniversalDependencies/UD_Chinese-HK) |
| **genre** | spoken |
| **contact** | tswong-c@my.cityu.edu.hk; jsylee@cityu.edu.hk |
| **sentences** | 1004 |
| **tokens** | 9874 |

**Issue draft:** [UD_Chinese-HK](../issue_drafts/UD_Chinese-HK.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A - spoken data only


## Metadata review

### corpus metadata

Parallel treebank with [UD_Cantonese-HK](UD_Cantonese-HK.html), linked via `parallel_id` (e.g. `hk/1`). Per the README, the 1004 sentences come from **4 distinct sources**, documented only in prose in the README, not in the `.conllu`:

| `sent_id` range | Proposed `document_id` | Title |
| --- | --- | --- |
| 1-410 | `missing_days` | Missing days / 小時光 ([film](https://www.youtube.com/watch?v=1qSMiw0vhzU)) |
| 411-547 | `tempo_in_temple` | Tempo in Temple / 廟眾樂樂 ([film](https://www.youtube.com/watch?v=8e8Lqd6grTE)) |
| 548-650 | `what_day_is_today` | What day is today / 今日星期幾 ([film](https://www.youtube.com/watch?v=bBGwxIDiZ_o)) |
| 651-1004 | `legco_president_election_2016` | Legislative Council presidential election meeting (2016-10-12) ([Hansard](https://www.legco.gov.hk/yr16-17/chinese/counmtg/hansard/cm20161012-translate-c.pdf), [webcast](https://webcast.legco.gov.hk/public/zh-hk/SearchResult?MeetingID=M16100003)) |

### transcription and annotation levels available

| Field | Advice |
|---|---|
| `translit` | change to `text_transliteration` |

### speaker metadata

_(none found)_ - no speaker distinction encoded, even though the legislative-council portion clearly involves multiple speakers.

### doc (and paragraphs) metadata

_(none found)_ - no `document_id`. Add `# document_id` at sentences 1, 411, 548, and 651, using the proposed ids in the table above (same ranges as its Cantonese-HK counterpart).

### modality metadata

_(none found)_ - not required for a single-modality (`only spoken`) treebank, but `# genre` (film/legislative-proceedings) could be added per document using the table above.
