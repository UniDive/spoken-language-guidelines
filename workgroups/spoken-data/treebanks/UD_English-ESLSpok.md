---
layout: base
title: 'English ESLSpok'
udver: '2'
---

# English ESLSpok

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.12 |
| **link** | [https://github.com/UniversalDependencies/UD_English-ESLSpok](https://github.com/UniversalDependencies/UD_English-ESLSpok) |
| **genre** | spoken |
| **contact** | kkyle2@uoregon.edu |
| **sentences** | 2320 |
| **tokens** | 21312 |

**Issue draft:** [UD_English-ESLSpok](../issue_drafts/UD_English-ESLSpok.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A

## Metadata review

### doc (and paragraphs) metadata

_(none found)_ - no `newdoc id` exists at all.

| Field | Advice |
|---|---|
| — | derive `# newdoc id` from the `sent_id` prefix (everything before `_<number>`, e.g. `file01243.txt`); recompose by sorting sentences within each prefix by that trailing number, which recovers a consistent (if sparse, since only a sample was taken) in-document order |


### speaker metadata

_(none found)_ - each document is one L2 English speaker's interview session; no `speaker_id` is encoded, though one could plausibly be derived from the same filename once `newdoc id` exists.
