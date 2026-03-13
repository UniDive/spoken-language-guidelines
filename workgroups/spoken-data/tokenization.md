---
layout: base
title:  'Tokenization and Word Segmentation'
udver: '2'
---

# Tokenization and Word Segmentation

TODO: what counts as a word in spoken treebanks?

@sylvainkahane:
* Elements that have a clear syntactic position
  * [ANONYM], Anonymized=Yes
  * [PERSON1], [PERSON2] or we give them names [CHR], [THO], …, [MOTHER], [KID]
  * [PLACE], [COUNTRY], [CITY], [STREET] …
  * special [SILENCE] token that can also constitute a sentence by itself and can take relations. Is [SILENCE]=[PAUSE] but with a different syntactic position?
  * onomatopeia: euh, pff, tss, … Problem of transcription (language-specific)
    * tsk
    * MT ee em mm qq / (aa)
    * MT eħe mhm (backchannels)

Elements that are generally not part of the syntactic construction (they can be as [SILENT])
[LAUGH]... punct + PUNCT, Pause=Yes, NonVerbal=Yes (very important for searches)
[INCOMPREHENSIBLE] : Do we want to indicate the approximative number of syllables?  SyllablesNumber=X
What relation? Indicate it if you can infer it, otherwise dep

* Silent pauses are a particular case. Two solutions are possible
  * Solution 1. Pauses are tokens: [PAUSE], Duration=205 (millisecond)
    * Examples in Rhapsodie: https://universal.grew.fr/?custom=68d64faccba6e
  * Solution 2. Pauses are features: PauseAfter=Yes

- short pauses
- non verbal behaviours (laughs, coughs, noises of any kind)
- use of punctuation
- Interrupted words
- Language specific documentation should include information about any specific transcription convention that has been followed.
  - For instance, for KIParla Forest: everything is lowercased, acronyms are transcribed as they are spelled out in speech
- anonymized items