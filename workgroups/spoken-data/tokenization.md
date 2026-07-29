---
layout: base
title:  'Tokenization and Word Segmentation'
udver: '2'
---

- [Tokenization and Word Segmentation](#tokenization-and-word-segmentation)
  - [Numbers and acronyms](#numbers-and-acronyms)
  - [Pauses](#pauses)
  - [Non-verbal behaviours](#non-verbal-behaviours)
  - [Anonymized/Pseudonymized tokens](#anonymizedpseudonymized-tokens)

# Tokenization and Word Segmentation

In general, we consider as a token those elements that have a clear syntactic position. Phenomena with no written counterpart — pauses, non-verbal noises, anonymized content — are only tokenized when they can be given such a position; otherwise they are represented as features on a neighbouring token, or not represented at all. The rest of this chapter goes through the main cases.

## Numbers and acronyms

Numbers can appear in a transcript either as figures or spelled out; in both cases they are annotated as `NUM`.

Acronyms, when transcribed as their phonetic realization, are a single token: for instance *esseoesse* for "S.O.S", as the acronym is pronounced in Italian.

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
