---
layout: base
title: 'Issue draft: Telugu_English TECT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Telugu_English TECT](../treebanks/UD_Telugu_English-TECT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Telugu_English-TECT](https://github.com/UniversalDependencies/UD_Telugu_English-TECT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Telugu_English-TECT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

The treebank is listed as `only spoken`, but the README says otherwise: sentences are drawn from three mixed sources - "edited data from the Telugu UD treebank" (written), "sentences from a grammar book" (written), and "spoken conversational utterances" from the MASSIVE/SLURP dataset.

**Finding:** No field distinguishes which source a given sentence comes from - `sent_id` is just a sequential number, and no other comment-level metadata exists.

**Suggestion:** Could you point us to which sentences are spoken vs. written, so `type`/`genre` and per-sentence `# modality` can be corrected?

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
