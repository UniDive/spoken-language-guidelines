---
layout: base
title:  'Morphology'
udver: '2'
---

- [Morphology](#morphology)
  - [Interrupted words, false starts, reparandum](#interrupted-words-false-starts-reparandum)
  - [Unintelligible material](#unintelligible-material)

# Morphology

## Interrupted words, false starts, reparandum

Interrupted words (repetitions, false starts, reformulations) are generally transcribed with a trailing `~` or `-`, and marked `Interrupted=Yes` in `MISC` — this feature is needed because a token can also legitimately end in `-` for other reasons (e.g. pre- and postposition).

As far as lemmatization and pos-tagging are concerned, two options are possible:

* lemmatizing with the same element as the form and adding upos `X`: in this case we suggest to encode the recoverable lemma and the recoverable part of speech, when possible, in MISC, by means of `ExtPos` and `ExtLemma`
* the lemma of the target form, when it is clearly recoverable from the morphosyntactic context (e.g. the word is almost complete, or the same stem is repeated nearby)

Syntactic relations are annotated when they can be inferred, otherwise `dep` is used.

## Unintelligible material

Unintelligible material is transcribed with corpus-specific conventions.
We suggest to mark this tokens as `Unintelligible=Yes` in MISC.
As far as lemmatization and postagging, the same strategies as *interrupted words* apply.