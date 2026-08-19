---
layout: base
title: 'Nenets Tundra'
udver: '2'
---

# Nenets Tundra

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                            |
| **available since** | 2.16                                                                                                                   |
| **link**            | [https://github.com/UniversalDependencies/UD_Nenets-Tundra](https://github.com/UniversalDependencies/UD_Nenets-Tundra) |
| **genre**           | spoken                                                                                                                 |
| **contact**         | <mus.nikolett@gmail.com>                                                                                               |
| **sentences**       | 170                                                                                                                    |
| **tokens**          | 1272                                                                                                                   |

**Issue draft:** [UD_Nenets-Tundra](../issue_drafts/UD_Nenets-Tundra.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### languages and translation(s)

| Field     | Advice               |
| --------- | -------------------- |
| `text_en` | change to `text_eng` |
| `text_ru` | change to `text_rus` |

### transcription and annotation levels available

| Field      | Advice                                 |
| ---------- | -------------------------------------- |
| `text_p`   | unclear                                |
| `translit` | change to `text_translitteration`      |
| `p_text`   | unclear, maybe also typo for `text_p`? |

### doc (and paragraphs) metadata

No `newdoc id` exists, but `doc_title_` already identifies the document and can be used directly to introduce it.

| Field        | Advice                                            |
| ------------ | ------------------------------------------------- |
| `doc_title_` | use as `# newdoc id` (rename/repurpose the field) |
| `media` | corpus-specific (doc-level) - verify against metadata.html |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### additional fields found by clone verification (2026-07-30)

| Field       | Advice                 |
| ----------- | ---------------------- |
| `sound_url` | move to document level |
