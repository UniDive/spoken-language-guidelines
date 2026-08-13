---
layout: base
title: 'Issue draft: South_Levantine_Arabic MADAR'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to South_Levantine_Arabic MADAR](../treebanks/UD_South_Levantine_Arabic-MADAR.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_South_Levantine_Arabic-MADAR](https://github.com/UniversalDependencies/UD_South_Levantine_Arabic-MADAR)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_South_Levantine_Arabic-MADAR`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

`genre` lists `spoken social`, but the README indicates the 100 sentences are actually written: they're manually translated (not transcribed) short conversational tourism-related texts from the MADAR Parallel Corpus, itself derived from the written Basic Traveling Expression Corpus (BTEC). We couldn't find any indication that a sentence is a transcription of actual speech.

**Suggestion:** Could you confirm whether any sentences are actually spoken, or should `spoken` be dropped from `genre`?

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
