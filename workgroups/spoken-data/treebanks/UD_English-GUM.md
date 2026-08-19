---
layout: base
title: 'English GUM'
udver: '2'
---

# English GUM

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | mixed |
| **available since** | 2.2 |
| **link** | [https://github.com/UniversalDependencies/UD_English-GUM](https://github.com/UniversalDependencies/UD_English-GUM) |
| **genre** | academic blog email fiction government legal news nonfiction social spoken web wiki |
| **contact** | amir.zeldes@georgetown.edu |
| **sentences** | 14353 |
| **tokens** | 252284 |

**Issue draft:** [UD_English-GUM](../issue_drafts/UD_English-GUM.html)

## Modality identification

**Is spoken part clearly identifiable?** yes - via `meta::genre`. Checked directly against `en_gum-ud-dev.conllu` and `en_gum-ud-test.conllu` (dev: 30 documents/1575 sentences, test: 30 documents/1464 sentences; 15 genres, 2 documents each per split). Of the 15 genres, 5 are spoken: `vlog`, `speech`, `podcast`, `court`, `conversation`


The other 10 genres (`academic`, `bio`, `essay`, `fiction`, `interview`, `letter`, `news`, `textbook`, `voyage`, `whow`) are written or mixed-modality (e.g. `interview` here is written Q&A, not transcribed speech).

**Advise:** add `# modality = spoken` to the genres listed above and `# modality = written` to the rest, per the [Document-level metadata conventions](../metadata.html#document-level). .

**Interaction parameters (optional add-on):** checked source/summary metadata for one document per spoken genre to ground the proposal below :

| Genre          | `degree_of_spontaneity` | `number_of_participants` | `context`    | `setting`    | `channels`                       | `symmetry` |
| -------------- | ----------------------- | ------------------------ | ------------ | ------------ | -------------------------------- | ---------- |
| `conversation` | unplanned               | dialogic/multi-party     | private      | face-to-face | phonic-auditory; gestural-visual | symmetric  |
| `court`        | planned                 | multi-party              | professional | face-to-face | phonic-auditory; gestural-visual | asymmetric |
| `podcast`      | unplanned               | multi-party              | public       | online       | phonic-auditory                  | asymmetric |
| `speech`       | planned                 | monologic                | public       | broadcast    | phonic-auditory; gestural-visual | asymmetric |
| `vlog`         | planned                 | monologic                | public       | online       | phonic-auditory; gestural-visual | asymmetric |

Notes: `conversation` is Santa Barbara Corpus audio (no video) of private family/partner talk; `court` is audio-only Supreme Court oral argument (live Q&A elicited by justices' questions, hence `elicited` rather than `unplanned`); `podcast` (Global Voices) has editors plus 2 guests, audio-only; `speech` and `vlog` are both video-recorded (C-SPAN and YouTube respectively) with a single speaker/creator addressing an audience with no back-and-forth, hence `asymmetric`.

## Metadata review

### speaker metadata

| Field | Advice |
|---|---|
| `speaker` | change to `speaker_id` |

### doc (and paragraphs) metadata

| Field | Advice |
|---|---|
| `newdoc id` | OK |

### modality metadata

| Field | Advice |
|---|---|
| `meta::genre` | consider switching to `genre` |
