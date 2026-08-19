---
layout: base
title: 'Turkish_German SAGT'
udver: '2'
---

# Turkish_German SAGT

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                        |
| **available since** | 2.7                                                                                                                                |
| **link**            | [https://github.com/UniversalDependencies/UD_Turkish_German-SAGT](https://github.com/UniversalDependencies/UD_Turkish_German-SAGT) |
| **genre**           | spoken                                                                                                                             |
| **contact**         | <ozlem@ims.uni-stuttgart.de>                                                                                                       |
| **sentences**       | 2184                                                                                                                               |
| **tokens**          | 36934                                                                                                                              |

**Issue draft:** [UD_Turkish_German-SAGT](../issue_drafts/UD_Turkish_German-SAGT.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### doc (and paragraphs) metadata

No `document_id` exists, but it can be derived directly from the `sent_id` prefix: `sent_id` follows `<doc-id>-<number>` (e.g. `TRDE-CS-C15-0001`), with 48 distinct document ids (`TRDE-CS-C01` ... `TRDE-CS-V06`).

| Field | Advice                                                                                      |
| ----- | ------------------------------------------------------------------------------------------- |
| —     | derive `# document_id` from the `sent_id` prefix (everything before the trailing `-<number>`) |

### sent metadata

| Field | Advice |
| --- | --- |
| `NOTE` | corpus-specific (sentence-level) - verify against metadata.html |
| `annotated with partaxis` | corpus-specific (sentence-level) - verify against metadata.html |
