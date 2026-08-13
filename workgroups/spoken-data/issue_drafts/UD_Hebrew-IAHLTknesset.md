---
layout: base
title: 'Issue draft: Hebrew IAHLTknesset'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Hebrew IAHLTknesset](../treebanks/UD_Hebrew-IAHLTknesset.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Hebrew-IAHLTknesset](https://github.com/UniversalDependencies/UD_Hebrew-IAHLTknesset)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Hebrew-IAHLTknesset`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (a reasonable guess):

**Finding:** The entire treebank may already be spoken (transcribed Knesset/parliament proceedings), rather than a partial split.

**Evidence:** `newdoc id` values follow `<year>_<doctype>_<id>` where `doctype` is only ever `ptv` (65 docs, likely 'protocol verbatim') or `ptm` (35 docs, likely 'protocol minutes') - both are transcribed parliamentary speech, not a spoken/written split.

**Suggestion:** Rather than partially tagging, please confirm whether the whole corpus should carry `# modality = spoken` (as transcribed parliamentary speech), or whether `ptm` (minutes, possibly edited/summarized) should be excluded as not verbatim spoken language.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion             |
| ----------- | ---------------------- |
| `newdoc id` | OK - already standard  |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion             |
| --------- | ----------------------- |
| `speaker` | change to `speaker_id` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
