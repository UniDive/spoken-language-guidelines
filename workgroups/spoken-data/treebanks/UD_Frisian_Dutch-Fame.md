---
layout: base
title: 'Frisian_Dutch Fame'
udver: '2'
---

# Frisian_Dutch Fame

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                      |
| **available since** | 2.8                                                                                                                              |
| **link**            | [https://github.com/UniversalDependencies/UD_Frisian_Dutch-Fame](https://github.com/UniversalDependencies/UD_Frisian_Dutch-Fame) |
| **genre**           | spoken                                                                                                                           |
| **contact**         | <a.r.y.braggaar@student.rug.nl>                                                                                                  |
| **sentences**       | 400                                                                                                                              |
| **tokens**          | 3729                                                                                                                             |

**Issue draft:** [UD_Frisian_Dutch-Fame](../issue_drafts/UD_Frisian_Dutch-Fame.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

(none found)

### transcription and annotation levels available

| Field         | Advice |
| ------------- | ------ |
| `text_switch` | OK     |

### speaker metadata

`speaker` is a composite/slash-separated string packing three pieces of metadata in one field, e.g. `fr/female/sp0013f`, `fr/child/sp0061c`: `<language variety>/<gender-or-age category>/<speaker code>` (the code's trailing letter redundantly repeats the category: `f`/`m`/`c`). Should be split into separate fields rather than simply renamed.

| Field                                                                 | Advice                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `speaker` (3rd segment, e.g. `sp0013f`)                               | split out and rename to `speaker_id`                                                                                                                                                                                                                                            |
| `speaker` (2nd segment: `male`/`female`/`child`, 285/114/2 sentences) | split out and rename to `speaker_gender` (`child` doesn't fit a gender value - would need `speaker_age` instead for those 2 sentences, please confirm)                                                                                                                          |
| `speaker` (1st segment: `fr`/`nl`)                                    | split out; not a standard metadata.md field - stable per speaker (142/143 codes have only one value), likely the speaker's dominant/native language variety in this Frisian-Dutch bilingual corpus - please confirm and propose a name (e.g. corpus-specific `speaker_variety`) |

### doc (and paragraphs) metadata

| Field       | Advice                                                                                                                                 |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `newdoc id` | OK - already standard, and already one-per-sentence here (400 documents, each a single standalone utterance - no recomposition needed) |
