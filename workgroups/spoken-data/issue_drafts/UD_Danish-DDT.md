---
layout: base
title: 'Issue draft: Danish DDT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Danish DDT](../treebanks/UD_Danish-DDT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Danish-DDT](https://github.com/UniversalDependencies/UD_Danish-DDT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Danish-DDT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?
This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken, and we could not find any usable signal: there is no `document_id`, and `sent_id` is just a sequential counter (`train-v2-0`, `train-v2-1`, ...) with no genre/source information.

**Suggestion:** Could `# modality` (or `# genre`) be added per document/sentence, so the spoken portion can be identified programmatically?

### Implementation notes

**Quick search & replace**
- None.

**Needs a small script**
- None currently possible - there's no usable signal (`document_id` doesn't exist and `sent_id` is a bare sequential counter) to key a script off, so no automated modality/genre tagging can be built until the maintainers can point at a source for this information.

**Needs manual input from maintainers**
- Whether `# modality` or `# genre` can be added at all, and if so, from what source (e.g. is there an internal mapping from sentence to original text/document that isn't currently exported to the `.conllu`?). This is the entire blocker here.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
