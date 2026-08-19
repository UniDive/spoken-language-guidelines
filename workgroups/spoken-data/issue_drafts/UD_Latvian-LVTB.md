---
layout: base
title: 'Issue draft: Latvian LVTB'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Latvian LVTB](../treebanks/UD_Latvian-LVTB.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Latvian-LVTB](https://github.com/UniversalDependencies/UD_Latvian-LVTB)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Latvian-LVTB`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material (`genre` includes `spoken` alongside `news`, `fiction`, `legal`, `academic`) but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (no signal found):

**Finding:** No genre-like field, `document_id`, or other comment-level metadata that would let us separate spoken from written sentences was found.

**Suggestion:** Could you point us to which sentences/documents are spoken vs. written?

No further outstanding metadata items were flagged for this treebank in the latest review.

### Implementation notes

**Needs manual input from maintainers**
- Modality: no `document_id` or genre-like comment metadata found at all, so no automatic detection was possible - need pointers to which sentences/documents are spoken vs. written (`genre = spoken` is only a value in the current genre field, not a per-sentence/document marker). Once that pointer exists, tagging is a one-line `harmonize_metadata.py tag-modality` or `rename-comment` run, but there's nothing to script against yet.
