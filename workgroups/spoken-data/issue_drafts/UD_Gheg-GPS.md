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

### Implementation notes

- **Quick search & replace:** `Lang`→`Lang` is already the standard name, no action needed (kept in the table only for completeness).
- **Needs a small script:**
  - Deriving `# newdoc id` from `sent_id`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc DIR --pattern '^(?P<doc>.+)_\d+$' --write` - verified against `aln_gps-ud-test.conllu`, produces exactly 64 documents, matching the draft's "64 recordings" figure.
  - Adding `# genre = narrative` at document level once `newdoc id` exists: this is a constant value for every document, so simplest as a one-line loop inserting the comment after each `# newdoc id` line (not a `harmonize_metadata.py` op today - `tag-modality`-style logic but with a fixed value rather than a regex-conditioned one; a ~10-line variant would do it).
  - `speaker_residence` from the `P`/`Z` sent_id component: once newdoc ids exist, this is a `derive-newdoc`-style regex extraction (`P` → `Prishtina`, `Z` → `Zurich`) - straightforward but not yet covered by an existing subcommand.
- **Needs manual input from maintainers:** whether per-speaker age is available (would enable `speaker_age`) or only the generational bucket (`speaker_generation` ∈ `G1`/`G2`/`G3`) - the latter is derivable by script from the `newdoc id`/`sent_id` prefix once confirmed as the right field to add.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
