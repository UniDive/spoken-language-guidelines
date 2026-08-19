---
layout: base
title: 'Gheg GPS'
udver: '2'
---

# Gheg GPS

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| **type**            | only spoken                                                                                                  |
| **available since** | 2.11                                                                                                         |
| **link**            | [https://github.com/UniversalDependencies/UD_Gheg-GPS](https://github.com/UniversalDependencies/UD_Gheg-GPS) |
| **genre**           | spoken                                                                                                       |
| **contributors**         | Ebert, Christian; Islamaj, Artan; Kuqi, Adrian; Sonnenhauser, Barbara; Widmer, Paul; Plamada, Magdalena |
| **sentences**       | 966                                                                                                          |
| **tokens**          | 15990                                                                                                        |

**Issue draft:** [UD_Gheg-GPS](../issue_drafts/UD_Gheg-GPS.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### speaker metadata

Location (`P` Prishtina / `Z` Zurich) and generation (`G1`/`G2`/`G3`) are encoded in the `sent_id`/derived `document_id` prefix but not as explicit metadata fields. Speaker age ranges from 10 to 67, but is only reported corpus-wide in the README, not per speaker in the data.

| Field | Advice                                                                                                                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| —     | consider adding `speaker_residence` (`Prishtina`/`Zurich`), derived from the `P`/`Z` sent_id component                                                                             |
| —     | consider a corpus-specific `speaker_generation` field (`G1`/`G2`/`G3`) - the three-generation design isn't captured by `speaker_age` alone; no existing standard field covers this |
| —     | add `speaker_age` if per-speaker ages are available (currently only a corpus-wide range, 10-67, is documented)                                                                     |

### doc (and paragraphs) metadata

no `document_id` exists, but `sent_id` already encodes it: format `<Location>-<Generation>-<SpeakerID>_<N>` (e.g. `P-G1-01_1`), where `Location` ∈ {`P` Prishtina, `Z` Zurich} and `Generation` ∈ {`G1`, `G2`, `G3`}. The prefix before the trailing `_<N>` identifies one interview/recording (64 recordings total, each re-narrating the *Pear Stories* video).

| Field | Advice                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------- |
| —     | derive `# document_id` from the `sent_id` prefix (everything before the trailing `_<number>`)              |
| —     | add `# genre = narrative` at document level (elicited re-narration of the *Pear Stories* stimulus video) |
