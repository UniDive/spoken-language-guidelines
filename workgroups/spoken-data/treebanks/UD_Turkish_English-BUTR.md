---
layout: base
title: 'Turkish_English BUTR'
udver: '2'
---

# Turkish_English BUTR

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | only spoken                                                                                                                          |
| **available since** | 2.16                                                                                                                                 |
| **link**            | [https://github.com/UniversalDependencies/UD_Turkish_English-BUTR](https://github.com/UniversalDependencies/UD_Turkish_English-BUTR) |
| **genre**           | spoken                                                                                                                               |
| **contributors**         | Akkurt, Furkan; Teker, Nursena; Binici, Helin; Demir, Ahmet; Sampanis, Konstantinos |
| **sentences**       | 58                                                                                                                                   |
| **tokens**          | 441                                                                                                                                  |

**Issue draft:** [UD_Turkish_English-BUTR](../issue_drafts/UD_Turkish_English-BUTR.html)

## Modality identification

**Is spoken part clearly identifiable?** No - `type` says `only spoken`, but the corpus is actually mixed. The README documents `# medium` as "Communication medium (Written or Spoken), where known", and in the data it's only present on 19 of 58 sentences (`Spoken` or `Written`) - not all sentences are identifiable as spoken or written.

## Metadata review

### modality metadata

_(none found)_ - `medium` (present on 19/58 sentences, values `Spoken`/`Written`) is exactly a modality field and should be renamed/lowercased to `# modality = spoken`/`# modality = written`; the remaining 39 sentences have no modality marked at all.

### sent metadata

| Field     | Advice                                                                                                                                        |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `text_en` | OK (ISO 639-1 two-letter code)                                                               |
| `medium`  | rename to `# modality` (values `spoken`/`written`, lowercase); only present on 19/58 sentences - ask maintainer if the rest can be classified |
