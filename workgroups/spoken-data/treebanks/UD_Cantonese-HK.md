---
layout: base
title: 'Cantonese HK'
udver: '2'
---

# Cantonese HK

[Back to index](ud_spoken_treebanks.html)

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

**Is spoken part clearly identifiable?** N/A

*Re-checked directly against `yue_hk-ud-test.conllu` and the repo README - the README documents rich source/genre/fluency information per `sent_id` range that is not currently encoded as CoNLL-U metadata at all.*

## Metadata review

### corpus metadata

This is a parallel treebank with [UD_Chinese-HK](UD_Chinese-HK.html) (same sentences, Cantonese vs. Mandarin), linked via `parallel_id` (e.g. `hk/1`). Per the README, the 1004 sentences come from **4 distinct sources**, documented only in prose in the README, not in the `.conllu`:

| `sent_id` range | Title | Source | Fluency |
|---|---|---|---|
| 1-410 | Missing days / 小時光 | [YouTube film](https://www.youtube.com/watch?v=1qSMiw0vhzU) | mostly prepared dialogue |
| 411-547 | Tempo in Temple / 廟眾樂樂 | [YouTube film](https://www.youtube.com/watch?v=8e8Lqd6grTE) | spontaneous interview, many disfluencies/reparandums |
| 548-650 | What day is today / 今日星期幾 | [YouTube film](https://www.youtube.com/watch?v=bBGwxIDiZ_o) | mostly prepared, contains dead air |
| 651-1004 | Legislative Council presidential election meeting (2016-10-12) | [Hansard](https://www.legco.gov.hk/yr16-17/chinese/counmtg/hansard/cm20161012-translate-c.pdf), [webcast](https://webcast.legco.gov.hk/public/zh-hk/SearchResult?MeetingID=M16100003) | spontaneous discussion, many disfluencies/reparandums |



### speaker metadata

_(none found)_ - no speaker distinction encoded, even though the legislative-council portion clearly involves multiple speakers.

### doc (and paragraphs) metadata

_(none found)_ - no `newdoc id` (or the `_filename` this page previously listed; it is **not** present in the current `.conllu`, that was stale). Given the table above, `# newdoc id` could be set at sentences 1, 411, 548, and 651, one per source.

### modality metadata

_(none found)_ - not required for a single-modality (`only spoken`) treebank, but `# genre` (film/interview/legislative-proceedings) and interaction parameters (`degree_of_spontaneity = planned` for the three films vs. `unplanned` for the legislative discussion) could be added per document using the table above.

### sent metadata

| Field | Advice |
|---|---|
| `parallel_id` | keep |

### varia (all corpus specific)

_(none found)_

### token-level metadata (MISC)

| Field | Advice |
|---|---|
| `SpaceAfter` | n/a (standard UD feature, not spoken-specific) |
| `Translit` | keep (corpus-specific) |
| `Gloss` | keep (corpus-specific) |

