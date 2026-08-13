---
layout: base
title: 'Issue draft: Ukrainian ParlaMint'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Ukrainian ParlaMint](../treebanks/UD_Ukrainian-ParlaMint.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint](https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Ukrainian-ParlaMint`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

Yes - the entire corpus should be `# modality = spoken`. The README describes it as "Ukrainian parliamentary plenary session transcripts" drawn from ParlaMint-UA and other open sources (NSDC); there's no written material.

**Suggestion:** Add `# modality = spoken` corpus-wide.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

`newdoc id` already exists for the ParlaMint-sourced sentences (one per utterance, e.g. `ParlaMint-UA_2022-01-25-m0.u100`), but is entirely missing for the 502 sentences sourced from NSDC (`sent_id` like `NSDC_UA_28_Feb2014-1`). These can easily get a `newdoc id` too, derived from the `sent_id` prefix (everything before the trailing `-<number>`) - all 502 collapse to a single document, `NSDC_UA_28_Feb2014`.

| Field | Suggestion                                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |
| —     | derive `# newdoc id = NSDC_UA_28_Feb2014` for the NSDC-sourced sentences (`sent_id` prefix before the trailing `-<number>`) |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

`text_en` and `phonetic_text` each appear exactly once across the entire corpus, both with the literal placeholder value `undefined undefined` - these look like leftover template artifacts rather than real content.

| Field           | Suggestion                                                                         |
| --------------- | ---------------------------------------------------------------------------------- |
| `text_en`       | remove (single occurrence, placeholder value `undefined undefined`) |
| `phonetic_text` | remove (single occurrence, placeholder value `undefined undefined`) |
| `WARNING`       | corpus-specific (sentence-level, parser-diagnostic comments e.g. dependency-cycle warnings) - verify against metadata.html |

### 4. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field  | Suggestion                                                                   |
| ------ | ---------------------------------------------------------------------------- |
| `lang` | rename to `Lang` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
