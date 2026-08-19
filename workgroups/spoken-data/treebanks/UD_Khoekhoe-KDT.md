---
layout: base
title: 'Khoekhoe KDT'
udver: '2'
---

# Khoekhoe KDT

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                |
| **available since** | 2.16                                                                                                                 |
| **link**            | [https://github.com/UniversalDependencies/UD_Khoekhoe-KDT](https://github.com/UniversalDependencies/UD_Khoekhoe-KDT) |
| **genre**           | fiction grammar-examples spoken                                                                                      |
| **contact**         | <kira.tulchynska@mail.huji.ac.il>, <witzlack@gmail.com>                                                              |
| **sentences**       | 3589                                                                                                                 |
| **tokens**          | 27611                                                                                                                |

**Issue draft:** [UD_Khoekhoe-KDT](../issue_drafts/UD_Khoekhoe-KDT.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - via the `document_id` prefix, which names the source type: `book` (15), `grammar` (2), `film` (2), `conversation` (1). `conversation` and `film` (transcribed dialogue/subtitles) are plausibly spoken; `book`/`grammar` are written - please confirm whether `film` here means subtitle/transcript text.

## Metadata review

### languages and translation(s)

| Field     | Advice               |
| --------- | -------------------- |
| `english` | change to `text_eng` |
| `parallel_id` | corpus-specific (sentence-level) - verify against metadata.html |

### token-level metadata (MISC)

| Field | Advice |
| --- | --- |
| `OrigLang` | rename to `OrigLang` |
| `Lang` | rename to `Lang` |
