---
layout: base
title: 'Komi_Zyrian IKDP'
udver: '2'
---

# Komi_Zyrian IKDP

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                  |
| **available since** | 2.2                                                                                                                          |
| **link**            | [https://github.com/UniversalDependencies/UD_Komi_Zyrian-IKDP](https://github.com/UniversalDependencies/UD_Komi_Zyrian-IKDP) |
| **genre**           | spoken                                                                                                                       |
| **contact**         | <nikotapiopartanen@gmail.com>                                                                                                |
| **sentences**       | 214                                                                                                                          |
| **tokens**          | 2304                                                                                                                         |

**Issue draft:** [UD_Komi_Zyrian-IKDP](../issue_drafts/UD_Komi_Zyrian-IKDP.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### corpus metadata

| Field            | Advice |
| ---------------- | ------ |
| `corpus_version` | keep   |

### languages and translation(s)

| Field      | Advice             |
| ---------- | ------------------ |
| `text_en`  | make tags: text_en |
| `text_ru`  | text_rus           |
| `text_end` | text_en            |

### transcription and annotation levels available

(none found)

### speaker metadata

(none found)

### doc (and paragraphs) metadata

_(none found)_ - no `newdoc id` exists, but per the README, `sent_id` values match those in the archived IKDP corpus, with `+` marking sentence IDs that span multiple annotations (i.e. a merge within one recording, not a document boundary). This suggests `sent_id` already encodes a document/recording identifier that `newdoc id` could be derived from.

| Field | Advice                                                                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` prefix identifying the source recording (please confirm the exact delimiter with the maintainer); treat `+`-joined `sent_id`s as belonging to the same document |

### modality metadata

(none found)

### sent metadata

(none found)

### varia (all corpus specific)

| Field     | Advice |
| --------- | ------ |
| `comment` |        |
| `label`   |        |

### token-level metadata (MISC)

| Field        | Advice                                         |
| ------------ | ---------------------------------------------- |
| `GTtags`     | keep (corpus-specific)                         |
| `SpaceAfter` | n/a (standard UD feature, not spoken-specific) |
| `OrigLang`   | rename to `OrigLang`                           |
| `Lang`       | rename to `Lang`                               |
| `Note`       | keep (corpus-specific)                         |

### additional fields found by clone verification (2026-07-30)

(none found)
