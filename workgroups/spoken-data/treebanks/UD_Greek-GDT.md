---
layout: base
title: 'Greek GDT'
udver: '2'
---

# Greek GDT

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                          |
| **available since** | 1.1                                                                                                            |
| **link**            | [https://github.com/UniversalDependencies/UD_Greek-GDT](https://github.com/UniversalDependencies/UD_Greek-GDT) |
| **genre**           | news wiki spoken                                                                                               |
| **contact**         | <prokopis@ilsp.gr>                                                                                             |
| **sentences**       | 2521                                                                                                           |
| **tokens**          | 61773                                                                                                          |

**Issue draft:** [UD_Greek-GDT](../issue_drafts/UD_Greek-GDT.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - via the source-outlet component embedded in `newdoc id` (`gdt-<date>-<source>-<docname>`). Sentences with `ep` as the source (e.g. `gdt-20020204-ep-sessions_*-*`) are transcripts of European Parliament plenary sessions (45 docs); `ert`/`ertonline` (Greek public broadcaster) are also spoken/broadcast material.

## Metadata review

| Field       | Advice                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------- |
| `newdoc id` | make tags: doc_id                                                                                  |
| —           | add `# genre = speech` on `ep`-sourced documents (European Parliament plenary session transcripts) |
| —           | add `# genre = news` on `ert`/`ertonline`-sourced documents (broadcast news)                       |

### modality metadata

Add `# modality = spoken` on documents whose `newdoc id` source component is `ep`, `ert`, or `ertonline`.

**`ep`** (European Parliament plenary sessions, 45 docs): `degree_of_spontaneity = planned` (prepared parliamentary speeches), `number_of_participants = monologic` (one speaker per document/turn), `context = professional`, `setting = broadcast`, `symmetry = symmetric` (MEPs address the chamber under comparable roles).

**`ert`/`ertonline`** (Greek public broadcaster, 23 docs): `degree_of_spontaneity = planned` (scripted/read news bulletins), `number_of_participants = monologic` (single anchor/narrator, unless interview segments are present - please confirm), `context = public`, `setting = broadcast`, `symmetry = symmetric`.
