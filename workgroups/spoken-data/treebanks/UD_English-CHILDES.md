---
layout: base
title: 'English CHILDES'
udver: '2'
---

# English CHILDES

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.16 |
| **link** | [https://github.com/UniversalDependencies/UD_English-CHILDES](https://github.com/UniversalDependencies/UD_English-CHILDES) |
| **genre** | spoken |
| **contact** | xy236@georgetown.edu |
| **sentences** | 48183 |
| **tokens** | 289817 |

**Issue draft:** [UD_English-CHILDES](../issue_drafts/UD_English-CHILDES.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A


## Metadata review

### doc (and paragraphs) metadata

_(none found)_ - `corpus_name` (6 distinct values: `Brown`, `Braunwald`, `Providence`, `Kuczaj`, `Weist`, `Thomas`) is currently sentence-level and its sentences are interleaved throughout the file rather than grouped.

| Field | Advice |
|---|---|
| `corpus_name` | recompose: sort sentences by `original_sent_id` within each `corpus_name`, then set `corpus_name` once per document as `# newdoc id` |

**Caveat to confirm with maintainer:** `corpus_name` is the CHILDES *study* name, not a single recording - e.g. `Brown` alone contains three different children (`Adam`, `Eve`, `Sarah`) recorded across different ages/sessions, and `Providence` contains three more (`Lily`, `Naima`, `Violet`). If a "document" should mean one recording session, `newdoc id` may need to key on `(corpus_name, child_name, child_age)` instead of `corpus_name` alone

### speaker metadata

| Field | Advice |
|---|---|
| `child_name` | rename to `speaker_id` |
| `child_age` | rename to `speaker_age` |
| `child_gender` | rename to `speaker_gender` |
| `chi l d` | **data bug**, not a real field: a single malformed line (`# chi l d = 37.29...`, 1 occurrence) - almost certainly a corrupted `child_age` entry; flag to maintainer |
