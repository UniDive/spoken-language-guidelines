---
layout: base
title:  'Morphology'
udver: '2'
---

- [Morphology](#morphology)
  - [Interrupted words, false starts, reparandum](#interrupted-words-false-starts-reparandum)
  - [Onomatopoeia](#onomatopoeia)
  - [Unintelligible material](#unintelligible-material)
  - [Lemmas](#lemmas)
  - [Part-of-Speech Tags](#part-of-speech-tags)

# Morphology

TODO: do we have something to say here besides the below? Possibly:
- some specifications about what to treat as an `INTJ` and what not, in particular for elements that have discourse functions

## Interrupted words, false starts, reparandum

Interrupted words (repetitions, false starts, reformulations) are transcribed with a trailing `~` or `-`, and marked `Interrupted=Yes` in `MISC` — this feature is needed because a token can also legitimately end in `-` for other reasons (e.g. pre- and postposition).

Their lemma can be either:

* the same as the form, or
* the lemma of the target form, but only when it is clearly recoverable from the morphosyntactic context (e.g. the word is almost complete, or the same stem is repeated nearby) — whether this should instead be captured with a dedicated `ExtLemma` feature is still to be discussed.

False starts are annotated with `upos=X` and `ExtPos=<upos-of-the-target>` ([example](https://universal.grew.fr/?custom=6a3b66e04bed8)); `ExtPos` can be left empty when the reconstruction of the target word is unclear.

## Onomatopoeia

Open problem: what lemma and what POS should onomatopoeic items receive?

## Unintelligible material

Unintelligible material is generally transcribed as `x`, with lemma `x`; POS and syntactic relation are annotated when they can be inferred, otherwise left unspecified.

For languages, or transcription conventions, where `x` is not a suitable placeholder, the feature `Unintelligible=Yes` should be added to `MISC` instead.

## Lemmas

## Part-of-Speech Tags
