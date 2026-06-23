---
layout: base
title:  'Spoken Language Treebanks'
udver: '2'
---

Disclaimer: This page represents the output of UniDive WG1 T1.5 group. It is not meant to be understood as proper guidelines yet, it will evolve into UD guidelines in the future.

# Guidelines for Spoken Language UD Treebanks


* Basic principles
  * [Maximal unit segmentation](maximal_unit_segmentation.html)
  * [Tokenization and word segmentation](tokenization.html)
    * pauses (filled vs. silent vs. long), non-verbal behaviours and punctuation and anonymization/pseudonymization, incomprehensible speech signal
    * repetitions, false starts, reformulations, reparandum stuff
  * [Morphology](morphology.html)
    * interrupted words, lemmas
    * what is INTJ
  * [Syntax](syntax.html)
    * [specific syntax](specific_syntax.html)
    * co-constructed syntax and handling of overlap (in [Syntax](syntax.html))
    * question answering
  * [Speech specific metadata](metadata.html)
  * [CoNLL-U format and treebank structure](treebank_structure.html)

* Documentation of tags, features and relations
  * POS tags:
    * [PUNCT](PUNCT.html)
  * Syntactic relations:
    * `conj:reform`
    * [Discourse relation]
      * `discourse:backchannel`
      * `discourse:filledpause`
      * `discouse:filler`
    * [Parataxis]
      * `parataxis:insert`
      * `parataxis:parent`
    * reparandum

  * [MISC attributes](MISC.html)

* [Miscellanea](miscellanea.html)

* [Current UD Spoken treebanks](ud_spoken_treebanks.html)

to do: 
- Maximal unit segmentation  -> to refine 
- Tokenization -> to discuss together in toto, comment on doc and add examples
- Morphology -> to discuss together in toto, comment on doc and add examples
- Syntax -> to discuss together (except coconstruction)
- Metadata -> to refine, group pullrequests
- Discourse relation -> to discuss together