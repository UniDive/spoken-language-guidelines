---
layout: base
title: 'Scottish_Gaelic ARCOSG'
udver: '2'
---

# Scottish_Gaelic ARCOSG

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                                    |
| **available since** | 2.5                                                                                                                                      |
| **link**            | [https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG](https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG) |
| **genre**           | nonfiction fiction news spoken                                                                                                           |
| **contact**         | <colin.r.batchelor@googlemail.com>                                                                                                       |
| **sentences**       | 4748                                                                                                                                     |
| **tokens**          | 86139                                                                                                                                    |

**Issue draft:** [UD_Scottish_Gaelic-ARCOSG](../issue_drafts/UD_Scottish_Gaelic-ARCOSG.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - the README explicitly describes 8 subcorpora, identifiable via the letter prefix of `newdoc id` (`<letters><digits>`, e.g. `c03`, `f08`, `fp09`, `n02`, `ns06`): `c` (Conversation - interview transcripts), `s` (Sport - radio commentary), `n` (Oral narrative), `ns` (News scripts, radio), `p` (Public interview/discussion, radio) are spoken; `f` (Fiction), `fp` (Formal prose), `pw` (Popular writing/newspaper columns) are written.

## Metadata review

### speaker metadata

| Field     | Advice                 |
| --------- | ---------------------- |
| `speaker` | change to `speaker_id` |

### modality metadata

add `# modality = spoken` to documents whose `newdoc id` prefix is `c`, `s`, `n`, `ns`, or `p`; `# modality = written` for `f`, `fp`, `pw`.

Per the README, each subcorpus also has a fairly clear genre and interaction profile:

| `newdoc id` prefix | Subcorpus                                                                  | `# genre`                                                 | Interaction parameters                                                                                                                                     |
| ------------------ | -------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `c`                | Conversation (interviews, Western Isles, 1998-2000)                        | `interview`                                               | `degree_of_spontaneity = unplanned`, `number_of_participants = dialogic`, `context = private`, `setting = face-to-face`, `symmetry = asymmetric`           |
| `s`                | Sport (_Radio nan Gàidheal_ match commentary)                              | `commentary`                                              | `degree_of_spontaneity = unplanned`, `number_of_participants = monologic`, `context = public`, `setting = broadcast`                                       |
| `n`                | Oral narrative (traditional stories)                                       | `narrative`                                               | `degree_of_spontaneity = planned`, `number_of_participants = monologic`, `context = public`, `setting = face-to-face`                                      |
| `ns`               | News scripts (_Radio nan Gàidheal_, early 1990s)                           | `radio show` (or `speech`)                                | `degree_of_spontaneity = planned` (scripted), `number_of_participants = monologic`, `context = public`, `setting = broadcast`                              |
| `p`                | Public interview/discussion (radio programmes, incl. political discussion) | `interview` (or `discussion` for the political programme) | `degree_of_spontaneity = unplanned`, `number_of_participants = dialogic`/`multi-party`, `context = public`, `setting = broadcast`, `symmetry = asymmetric` |
