---
layout: base
title: 'Greek Lesbian'
udver: '2'
---

# Greek Lesbian

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                  |
| **available since** | 2.16                                                                                                                   |
| **link**            | [https://github.com/UniversalDependencies/UD_Greek-Lesbian](https://github.com/UniversalDependencies/UD_Greek-Lesbian) |
| **genre**           | grammar-examples spoken fiction                                                                                        |
| **contact**         | <s.bompolas@athenarc.gr>                                                                                               |
| **sentences**       | 625                                                                                                                    |
| **tokens**          | 6624                                                                                                                   |

**Issue draft:** [UD_Greek-Lesbian](../issue_drafts/UD_Greek-Lesbian.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - via the `oral_corpus` field, which marks sentences drawn from audio recordings as opposed to published dictionaries/books.

## Metadata review

### modality metadata

add `# modality = spoken` to sentences where `oral_corpus` marks the source as an audio recording.

### additional fields found by clone verification (2026-07-30)

| Field      | Advice                                                                                                                                                                                                                                                                      |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source`   | for recording entries (`Recording (Date:..., Location:..., Gender:...)`), decompose into structured fields: `Gender` → `speaker_gender`, `Location` → `speaker_residence`, `Date` → corpus-specific (no standard field) - keep `source` as-is for dictionary/book citations |
| `text_el`  | rename to `text_ell` (ISO 639-3 code, see Sentence-level in metadata.html)                                                                                                                                                                                                  |
| `text__el` | typo                                                                                                                                                                                                                                                                        |
