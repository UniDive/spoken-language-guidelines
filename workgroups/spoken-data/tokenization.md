---
layout: base
title:  'Tokenization and Morphological annotation'
udver: '2'
---

- [Tokenization and Morphological annotation](#tokenization-and-morphological-annotation)
  - [Numbers](#numbers)
  - [Acronyms](#acronyms)
  - [Onomatopoeias](#onomatopoeias)
  - [Pauses](#pauses)
  - [Non-verbal behaviours](#non-verbal-behaviours)
  - [Anonymized/Pseudonymized tokens](#anonymizedpseudonymized-tokens)
  - [Added material (e.g., punctuation)](#added-material-eg-punctuation)
  - [Interrupted words, false starts, reparandum](#interrupted-words-false-starts-reparandum)
  - [Unintelligible material](#unintelligible-material)

# Tokenization and Morphological annotation

In general, we consider as a token those elements that have a clear syntactic position. Phenomena with no written counterpart — pauses, non-verbal noises, anonymized content — are only tokenized when they can be given such a position; otherwise they are represented as features on a neighbouring token, or not represented at all. The rest of this chapter goes through the main cases.

## Numbers

Numbers can appear in a transcript either as figures or spelled out; in both cases they are annotated as `NUM`.

## Acronyms

In some transcription standards, acronyms are rendered as their phonetic realization. For instance *esseoesse* or *esse o esse* for "S.O.S", as the acronym is pronounced in Italian.

In these cases, we recommend to treat the acronym as a single token in all cases, and normalize it to its standard spelling in the `form` field. The original transcription can be retained in `MISC` through the `OrigTranscription` feature.

## Onomatopoeias

Onomatopoeias they can serve multiple purposes and fill various morphosyntactic slots.

Our proposal is to tag them distributionally, assigning them the `upos` based on their function.

In a sentence like "and then we heard BOOM", `BOOM` is to be tagged as `NOUN` whereas in "il faut compter, euh, pff, l'équivalent de quarante euros, quelque chose comme ça." (en. "we need to consider, euh, pff, the equivalent of 40 euros, something like that.") `pff` is to be tagged as `INTJ`.

## Pauses

We distinguish three kinds of pause: silent, filled, and long. The following options are on the table:

* Encode short pauses — both silent and filled — as a feature on the preceding token, `PauseAfter=Silence|Filled`, without introducing a token of their own.
* Treat filled pauses (*euh*, *uh*, …) as regular tokens, tagged `INTJ` and attached with `discourse:filler`.
* Transcribe silent pauses as a dedicated token `[PAUSE]`, tagged `X`, attached with `discourse:pause`.

These strategies are not mutually exclusive: a treebank may, for instance, use `PauseAfter` for short pauses while still tokenizing longer silences as `[PAUSE]`.

## Non-verbal behaviours

Non-verbal behaviours (laughs, coughs, other noises) are not, by default, part of the syntactic construction.
In case the maintainers of the treebank want to include these elements as syntactic tokens, they are assigned upos `X`, dependency relation `dep` and they are marked by `NVB=Yes` in MISC.

## Anonymized/Pseudonymized tokens

Personal or otherwise sensitive information (names, places, institutions, etc.) is frequently anonymized or pseudonymized in spoken corpora. Such items generally have a clear syntactic position — they occupy an argument or adjunct slot just like the word they replace — and are therefore treated as ordinary tokens, integrated into the tree with the relation that fits their function.
We recommend to mark these tokens as `Anonymized=Yes` in MISC. In case of full anonymization, if the corpus has no other standard, we recommend generic english uppercased names such as [PLACE], [COUNTRY], [PERSON], [CITY]...
Category-specific placeholders are preferable whenever the corpus needs to preserve coreference between anonymized mentions (e.g. distinguishing two different anonymized speakers referred to later in the same conversation).

## Added material (e.g., punctuation)

Whenever tokens are added during the transcription/normalization phase, which are not actually part of the uttered speech, this should be declared in the general README of the treebank and it is a good practice to mark these tokens as `Added=Yes` in MISC.
This is typically the case of punctuation, which can be added either to make the text more similar to written standards, or to encode prosodic traits.

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