---
layout: base
title: 'Naija NSC'
udver: '2'
---

# Naija NSC

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                    |
| **available since** | 2.2                                                                                                            |
| **link**            | [https://github.com/UniversalDependencies/UD_Naija-NSC](https://github.com/UniversalDependencies/UD_Naija-NSC) |
| **genre**           | spoken                                                                                                         |
| **contact**         | <kim@gerdes.fr>                                                                                                |
| **sentences**       | 9241                                                                                                           |
| **tokens**          | 140837                                                                                                         |

**Issue draft:** [UD_Naija-NSC](../issue_drafts/UD_Naija-NSC.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

| Field     | Advice               |
| --------- | -------------------- |
| `text_en` | change to `text_eng` |

### transcription and annotation levels available

| Field        | Advice                        |
| ------------ | ----------------------------- |
| `text_ortho` | change to `text_orthographic` |

### speaker metadata

| Field                            | Advice |
| -------------------------------- | ------ |
| `speaker_id`                     | OK     |
| `speaker_education`              | OK     |
| `speaker_age`                    | OK     |
| `speaker_sex`                    | OK     |
| `speaker_residence`              | OK     |
| `speaker_naija_competency`       | OK     |
| `speaker_birthplace`             | OK     |
| `speaker_primary_other_language` | OK     |

### doc (and paragraphs) metadata

_(none found)_ - no `newdoc id` exists, but it can be derived from the `sent_id` prefix (please confirm the exact delimiter/recording identifier with the maintainer).

| Field | Advice                                                                          |
| ----- | ------------------------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` prefix identifying the source recording |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### additional fields found by clone verification (2026-07-30)

| Field       | Advice                          |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |
