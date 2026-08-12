---
layout: base
title: 'Pesh ChibErgIS'
udver: '2'
---

# Pesh ChibErgIS

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **type**            | only spoken                                                                                                              |
| **available since** | 2.15                                                                                                                     |
| **link**            | [https://github.com/UniversalDependencies/UD_Pesh-ChibErgIS](https://github.com/UniversalDependencies/UD_Pesh-ChibErgIS) |
| **genre**           | spoken                                                                                                                   |
| **contact**         | <natalia.caceres.arandia@cnrs.fr>                                                                                        |
| **sentences**       | 524                                                                                                                      |
| **tokens**          | 4275                                                                                                                     |

**Issue draft:** [UD_Pesh-ChibErgIS](../issue_drafts/UD_Pesh-ChibErgIS.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

| Field                | Advice               |
| -------------------- | -------------------- |
| `text_en`            | change to `text_eng` |
| `text_phrase-gls-es` | change to `text_spa` |

### transcription and annotation levels available

| Field                 | Advice                     |
| --------------------- | -------------------------- |
| `morphemic_text`      | change to `text_morphemic` |
| `text_phrase-gls-it`  | change to `text_phonetic`  |
| `text_phrase-gls-pro` | change to `text_prosodic`  |

### speaker metadata

| Field        | Advice |
| ------------ | ------ |
| `speaker_id` | OK     |

### doc (and paragraphs) metadata

_(none found)_ - no `newdoc id` exists, but it can be derived from the `sent_id` prefix (please confirm the exact delimiter/recording identifier with the maintainer).

| Field       | Advice                                                                          |
| ----------- | ------------------------------------------------------------------------------- |
| —           | derive `# newdoc id` from the `sent_id` prefix identifying the source recording |
| `sound_url` | move to document level                                                          |

### sent metadata

| Field           | Advice                                                                    |
| --------------- | ------------------------------------------------------------------------- |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |
