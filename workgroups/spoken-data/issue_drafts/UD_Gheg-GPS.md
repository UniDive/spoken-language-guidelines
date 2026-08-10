---
layout: base
title: 'Issue draft: Gheg GPS'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Gheg GPS](../treebanks/UD_Gheg-GPS.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Gheg-GPS](https://github.com/UniversalDependencies/UD_Gheg-GPS)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Gheg-GPS`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but `sent_id` already encodes it: format `<Location>-<Generation>-<SpeakerID>_<N>` (e.g. `P-G1-01_1`), where `Location` ∈ {`P` Prishtina, `Z` Zurich} and `Generation` ∈ {`G1`, `G2`, `G3`}. The prefix before the trailing `_<N>` identifies one interview/recording (64 recordings total, each re-narrating the *Pear Stories* video).

| Field | Suggestion                                                                                               |
| ----- | -------------------------------------------------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` prefix (everything before the trailing `_<number>`)              |
| —     | add `# genre = narrative` at document level (elicited re-narration of the *Pear Stories* stimulus video) |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

Location and generation are encoded in the `sent_id`/proposed `newdoc id` prefix but not as explicit speaker fields. Speaker age ranges from 10 to 67 across three generations, currently only documented corpus-wide.

| Field | Suggestion                                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| —     | consider adding `speaker_residence` (`Prishtina`/`Zurich`), derived from the `P`/`Z` sent_id component                                                                    |
| —     | consider a corpus-specific `speaker_generation` field (`G1`/`G2`/`G3`) - please confirm if per-speaker age is available, otherwise this preserves the generational design |
| —     | add `speaker_age` if per-speaker ages are available                                                                                                                       |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field  | Suggestion       |
| ------ | ---------------- |
| `Lang` | rename to `Lang` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
