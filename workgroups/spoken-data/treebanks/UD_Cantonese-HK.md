---
layout: base
title: 'Cantonese HK'
udver: '2'
---

# Cantonese HK

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.1 |
| **link** | [https://github.com/UniversalDependencies/UD_Cantonese-HK](https://github.com/UniversalDependencies/UD_Cantonese-HK) |
| **genre** | spoken |
| **contact** | tswong-c@my.cityu.edu.hk; jsylee@cityu.edu.hk |
| **sentences** | 1004 |
| **tokens** | 13918 |

**Issue draft:** [UD_Cantonese-HK](../issue_drafts/UD_Cantonese-HK.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A - spoken data only


## Metadata review

### corpus metadata

This is a parallel treebank with [UD_Chinese-HK](UD_Chinese-HK.html) (same sentences, Cantonese vs. Mandarin), linked via `parallel_id` (e.g. `hk/1`). Per the README, the 1004 sentences come from **4 distinct sources**, documented only in prose in the README, not in the `.conllu`:

| `sent_id` range | Proposed `document_id` | Title | Fluency |
| --- | --- | --- | --- |
| 1-410 | `missing_days` | Missing days / 小時光 ([film](https://www.youtube.com/watch?v=1qSMiw0vhzU)) | mostly prepared dialogue |
| 411-547 | `tempo_in_temple` | Tempo in Temple / 廟眾樂樂 ([film](https://www.youtube.com/watch?v=8e8Lqd6grTE)) | spontaneous interview, many disfluencies/reparandums |
| 548-650 | `what_day_is_today` | What day is today / 今日星期幾 ([film](https://www.youtube.com/watch?v=bBGwxIDiZ_o)) | mostly prepared, contains dead air |
| 651-1004 | `legco_president_election_2016` | Legislative Council presidential election meeting (2016-10-12) ([Hansard](https://www.legco.gov.hk/yr16-17/chinese/counmtg/hansard/cm20161012-translate-c.pdf), [webcast](https://webcast.legco.gov.hk/public/zh-hk/SearchResult?MeetingID=M16100003)) | spontaneous discussion, many disfluencies/reparandums |

### doc (and paragraphs) metadata

_(none found)_ - no `document_id` (or the `_filename` this page previously listed; it is **not** present in the current `.conllu`, that was stale). Add `# document_id` at sentences 1, 411, 548, and 651, using the proposed ids in the table above (please confirm the slugs - just short mnemonics derived from the titles).

### modality metadata

_(none found)_ - not required for a single-modality (`only spoken`) treebank, but `# genre` (film/interview/legislative-proceedings) and interaction parameters (`degree_of_spontaneity = planned` for the three films vs. `unplanned` for the legislative discussion) could be added per document using the table above.

