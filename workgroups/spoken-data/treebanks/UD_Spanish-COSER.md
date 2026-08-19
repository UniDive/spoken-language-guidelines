---
layout: base
title: 'Spanish COSER'
udver: '2'
---

# Spanish COSER

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                            |
| **available since** | 2.14                                                                                                                   |
| **link**            | [https://github.com/UniversalDependencies/UD_Spanish-COSER](https://github.com/UniversalDependencies/UD_Spanish-COSER) |
| **genre**           | spoken                                                                                                                 |
| **contributors**         | Bonilla, Johnatan |
| **sentences**       | 539                                                                                                                    |
| **tokens**          | 7987                                                                                                                   |

**Issue draft:** [UD_Spanish-COSER](../issue_drafts/UD_Spanish-COSER.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### doc (and paragraphs) metadata

the organization into documents is not clear from the data. Sentences come from two merged sources with different `sent_id` schemes: 474 use a dialect-region prefix (`anda-230`, `arag-...`, etc. - 17 distinct regions, too coarse to be a document) plus `orig_turn_id` (`<4-digit-id>-<turn>`, e.g. `1823-0229`); the other 65 use an ALEC-style `sent_id` (`ALEC_C11_Bo46_2`) with a `time` field instead of `turn_time`/`orig_turn_id`. The `orig_turn_id` prefix maps 1:1 to `location` in almost all cases, but one prefix (`3203`) spans 36 different locations, which breaks a clean derivation - please clarify the intended document/recording structure with the maintainer.

| Field       | Advice                                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `turn_time` | convert to milliseconds, split into `sound_alignment_begin` and `sound_alignment_end`; derive `duration`                             |
| `time`      | convert to milliseconds, split into `sound_alignment_begin` and `sound_alignment_end` (same as `turn_time`, different format/source) |
