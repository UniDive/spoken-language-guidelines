---
layout: base
title: 'Issue draft: French ParisStories'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to French ParisStories](../treebanks/UD_French-ParisStories.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_French-ParisStories](https://github.com/UniversalDependencies/UD_French-ParisStories)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_French-ParisStories`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but `sent_id` already encodes it: e.g. `ParisStories_2020_maisonAbondonnee_1` is document `ParisStories_2020_maisonAbondonnee`, sentence `1`. 86 distinct documents across 2776 sentences. `sound_url` is currently repeated per sentence (present on 2749/2776 sentences - 27 sentences in one document lack it).

| Field       | Suggestion                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------- |
| —           | derive `# newdoc id` from the `sent_id` prefix (everything before the trailing `_<number>`) |
| `sound_url` | move to document level, set once per `newdoc id`                                            |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion             |
| --------- | ---------------------- |
| `speaker` | rename to `speaker_id` |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field         | Suggestion                                                                              |
| ------------- | --------------------------------------------------------------------------------------- |
| `macrosyntax` | rename to `text_macrosyntax`                                                            |
| `tags`        | corpus-specific (only 1 occurrence, value `TODO`) - please confirm what this represents |

### 4. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### Implementation notes

- **Quick search & replace:** `speaker`→`speaker_id`, `macrosyntax`→`text_macrosyntax`, `AlignBegin`→`WordAlignmentBegin`, `AlignEnd`→`WordAlignmentEnd`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map speaker=speaker_id,macrosyntax=text_macrosyntax --write` and `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc DIR --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`.
- **Needs a small script:**
  - Deriving `# newdoc id` from `sent_id`: the simple `_<number>$` pattern misses ~40 sentences with `bis`-suffixed ids (e.g. `..._16bis`, `..._53bis`) - use `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc DIR --pattern '^(?P<doc>.+)_\d+[a-z]*$' --write` instead, which matches all sent_ids cleanly (0 mismatches, verified against all three release files plus `not-to-release/original_split/`).
  - Moving `sound_url` to document level: run `derive-newdoc` first (needed since no `newdoc id` currently exists), then `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url --write`. Dry-run on `fr_parisstories-ud-train.conllu` after deriving newdoc ids: 30/34 documents hoist cleanly, but 4 are flagged NOT constant (multiple distinct `sound_url` values within the same document) - those 4 need a maintainer look before hoisting (the 27 sentences the draft already notes as missing `sound_url` may be part of this).
- **Needs manual input from maintainers:** the `tags` field (1 occurrence, literal value `TODO`) - looks like a leftover placeholder rather than real data; could you confirm/remove it at the source?

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
