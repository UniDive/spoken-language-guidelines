---
layout: base
title: 'Polish LFG'
udver: '2'
---

# Polish LFG

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                            |
| **available since** | 2.2                                                                                                              |
| **link**            | [https://github.com/UniversalDependencies/UD_Polish-LFG](https://github.com/UniversalDependencies/UD_Polish-LFG) |
| **genre**           | fiction nonfiction news spoken social                                                                            |
| **contact**         | <aep@ipipan.waw.pl>, <adamp@ipipan.waw.pl>                                                                       |
| **sentences**       | 17246                                                                                                            |
| **tokens**          | 130967                                                                                                           |

**Issue draft:** [UD_Polish-LFG](../issue_drafts/UD_Polish-LFG.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - via the sentence-level `genre` field. `genre` (10 distinct values) includes `spoken (conversational)` (789), `spoken (prepared)` (306), `spoken (media)` (158) = 1,253 sentences, alongside `fiction` (7,252), `news` (6,744), `nonfiction` (1,273), `social` (526), `blog` (136), `academic` (51), `legal` (11).

## Metadata review

### corpus metadata

(none found)

### sent metadata

`genre` currently packs two things into one string: the top-level category (`spoken`) and a parenthetical sub-type (`conversational`, `prepared`, `media`). We suggest decomposing this into `# genre` plus the optional interaction-parameter layer:

| Field                               | Advice                                                                                                                           |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| —                                   | add `# modality = spoken` to sentences whose `genre` starts with `spoken`                                                        |
| `genre` (`spoken (conversational)`) | split into `# genre = conversation` + `# degree_of_spontaneity = unplanned`                                                      |
| `genre` (`spoken (prepared)`)       | split into `# genre = speech` + `# degree_of_spontaneity = planned`                                                              |
| `genre` (`spoken (media)`)          | split into `# genre = spoken` (or a more specific value, please confirm - radio show/TV show/podcast?) + `# setting = broadcast` |
| `This program is free software`     | corpus-specific (sentence-level) - verify against metadata.html                                                                  |
| `converted_from_file`               | corpus-specific (sentence-level) - verify against metadata.html                                                                  |
