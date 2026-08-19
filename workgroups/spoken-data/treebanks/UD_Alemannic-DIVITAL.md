---
layout: base
title: 'Alemannic DIVITAL'
udver: '2'
---

# Alemannic DIVITAL

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | mixed                                                                                                                          |
| **available since** | 2.17                                                                                                                           |
| **link**            | [https://github.com/UniversalDependencies/UD_Alemannic-DIVITAL](https://github.com/UniversalDependencies/UD_Alemannic-DIVITAL) |
| **genre**           | fiction nonfiction legal spoken wiki bible                                                                                     |
| **contributors**         | Beiner, Nathanaël; Hoff, Barbara; Bernhard, Delphine |
| **sentences**       | 977                                                                                                                            |
| **tokens**          | 19334                                                                                                                          |

**Issue draft:** [UD_Alemannic-DIVITAL](../issue_drafts/UD_Alemannic-DIVITAL.html)

## Modality identification

**Is spoken part clearly identifiable?** yes — via the `form` field: all 97 documents carry a `# form = ...` value (`dialog` 18, `mixed (form)` 38, `prose` 40, `verse` 1). Documents with `form = dialog` are spoken; all others (`mixed (form)`, `prose`, `verse`) are written.

**Advise:** add `# modality = spoken` to the 18 `form = dialog` documents and `# modality = written` to the remaining 79, per the [Document-level metadata conventions](../metadata.html#document-level).

## Metadata review

### doc (and paragraphs) metadata

| Field | Advice |
| --- | --- |
| `document_id` | OK |

### modality metadata

| Field | Advice |
| --- | --- |
| `channel` | we suggest to interpret channel as `phonic-auditory`, `gestural-visual` or `graphic-visual` |
| `genre` | OK |
| `form` | drives modality: `dialog` &rarr; add `# modality = spoken`; `prose`/`mixed (form)`/`verse` &rarr; add `# modality = written` |

### speaker metadata

| Field | Advice |
| --- | --- |
| `author` | rename to `speaker_id` |

### sent metadata

| Field | Advice |
| --- | --- |
| `language_variety` | corpus-specific (sentence-level) - verify against metadata.html |


