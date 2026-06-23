---
layout: base
title:  'PUNCT'
udver: '2'
---

# PUNCT

Guidelines for punctuation:
should be option and up to treebank creators to decide whether they want to include punctuation or not
if included:
we need to know how it was generated (field in MISC?), since spoken language does not have punctuation by design.
It could be part of the original transcript or script, or added as a form of annotation for prosody, or added semantically to help the parser.
Can we have a taxonomy of possible prosodic annotations so that different punctuation can be comparable? This could be the lemma even
SAME AS AUXILIARIES for PUNCT
LIST OF PROSODIC TRAITS - for now PAUSE or BREAK

Different uses of punctuation.
Punctuation can follow the conventions of written texts (that’s relevant for language with a written tradition).
Punctuation can be based on syntactic/pragmatic criteria (inspired by the properties of punctuation in written languages).
Punctuation can mimic the prosodic structure

Examples of written-like punctuations used in some 2.18 UD treebanks:
 - [English](https://spoken.grew.fr/?corpus_list=SP_UD_English-CHILDES%402.17%2CSP_UD_English-ESLSpok%402.17%2CSP_UD_English-GENTLE%402.17%2CSP_UD_English-GUM%402.17&request=pattern%20{%20X%20[upos="PUNCT"]%20}&clust1_key=X.form)
 - [French](https://universal.grew.fr/?corpus_list=UD_French-Rhapsodie@2.18,UD_French-ParisStories@2.18&request=pattern%20{%20X%20[upos="PUNCT"]%20}&clust1_key=X.form)
 - [Slovenian](https://universal.grew.fr/?corpus=UD_Slovenian-SST@2.18&request=pattern%20{%20X%20[upos="PUNCT"]%20}&clust1_key=X.form)

Examples of prosodic specific punctuations used in some 2.18 UD treebanks:
 - [Beja](https://universal.grew.fr/?corpus=UD_Beja-Autogramm@2.18&request=pattern%20{%20X%20[upos="PUNCT"]%20}&clust1_key=X.form)
 - [Hausa](https://universal.grew.fr/?corpus_list=UD_Hausa-NorthernAutogramm%402.18%2CUD_Hausa-SouthernAutogramm%402.18&request=pattern%20{%20X%20[upos="PUNCT"]%20}&clust1_key=X.form)
 - [Naija](https://universal.grew.fr/?corpus=UD_Naija-NSC@2.18&request=pattern%20{%20X%20[upos="PUNCT"]%20}&clust1_key=X.form)

