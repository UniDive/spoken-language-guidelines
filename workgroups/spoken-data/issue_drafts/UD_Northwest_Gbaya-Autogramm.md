---
layout: base
title: 'Issue draft: Northwest_Gbaya Autogramm'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Northwest_Gbaya Autogramm](../treebanks/UD_Northwest_Gbaya-Autogramm.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Northwest_Gbaya-Autogramm](https://github.com/UniversalDependencies/UD_Northwest_Gbaya-Autogramm)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Northwest_Gbaya-Autogramm`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                      |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field           | Suggestion                                                                |
| --------------- | ------------------------------------------------------------------------- |
| `phonetic_text` | change to `text_phonetic`                                                 |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### Implementation notes

**Quick search & replace**
- `phonetic_text` → `text_phonetic`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map phonetic_text=text_phonetic --write`
- `AlignBegin`/`AlignEnd` → `WordAlignmentBegin`/`WordAlignmentEnd` (token MISC): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`

**Needs a small script**
- `sound_url` → document level: the released file has no `# newdoc` markers at all, so document boundaries need to be reconstructed first from `sent_id` (format `GYA_..._NNN-NNN`), then `sound_url` can be hoisted:
  1. `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc DIR --pattern '^(?P<doc>.+)_[0-9]+[a-z]?[-_][0-9]+[a-z]?$' --write` — dry-run on the real file derives 3 `newdoc id`s (matching the 3 distinct `sound_url` values and the 3 source files under `not-to-release/`); one irregular `sent_id` (`..._098-098bb`) doesn't match this pattern and needs either a broader regex or a manual fix.
  2. `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write` — confirm no per-doc conflicts once step 1 is applied and reviewed.
  Given the "possibly" hedge in the draft, have a maintainer sanity-check the derived document boundaries before running with `--write`.
- `sent_timecode` → split into `sound_alignment_begin`, `sound_alignment_end`, `duration`: the first two are a plain split (`python3 workgroups/spoken-data/scripts/harmonize_metadata.py split-field DIR --key sent_timecode --sep ", " --into sound_alignment_begin,sound_alignment_end --write`, verified format `# sent_timecode = 2960, 4768`), but `duration` is a *computed* value (end − begin), not a split - that needs a short (~5 line) custom script on top, not currently covered by any subcommand.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
