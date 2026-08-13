---
layout: base
title: 'Telugu_English TECT'
udver: '2'
---

# Telugu_English TECT

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                        |
| **available since** | 2.14                                                                                                                               |
| **link**            | [https://github.com/UniversalDependencies/UD_Telugu_English-TECT](https://github.com/UniversalDependencies/UD_Telugu_English-TECT) |
| **genre**           | spoken                                                                                                                             |
| **contact**         | <anishka18v@gmail.com>                                                                                                             |
| **sentences**       | 97                                                                                                                                 |
| **tokens**          | 456                                                                                                                                |

**Issue draft:** [UD_Telugu_English-TECT](../issue_drafts/UD_Telugu_English-TECT.html)

## Modality identification

**Is spoken part clearly identifiable?** No - `type` says `only spoken`, but the README says otherwise: sentences are drawn from three mixed sources - "edited data from the Telugu UD treebank" (written), "sentences from a grammar book" (written), and "spoken conversational utterances" from the MASSIVE/SLURP dataset. There's no field distinguishing which source a given sentence comes from (`sent_id` is just a sequential number, and no other comment-level metadata exists) - flagged to maintainers to confirm which sentences are spoken vs. written.
