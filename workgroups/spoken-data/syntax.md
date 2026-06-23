---
layout: base
title:  'Morphology'
udver: '2'
---

# Syntax

## Co-constructed syntax

We consider as co-constructions those syntactic relations (without any restrictions) that hold between utterances produced (i) by different speakers or (ii) by the same speaker but after an interruption by another speaker. In interactive scenarios, indeed, multiple speakers may intertwine their utterances, sometimes even perfectly overlapping (Lerner 1991, Sacks 1992, Ono & Thompson 1996, Helasvuo 2004, Calabria 2023)

A coconstruction is encoded by a feature on the root of the second utterance indicating the syntactic role of the second utterance towards the first utterance, the sent-id of the first utterance, and the token-id of the governor of the second utterance:

`Coconstruct=<deprel>::<sent-id>::<token-id>`

### Typology of coconstructions

TODO: integrate with new material (@caterinamauri @elozucchini)

When the co-construction involves two or more different speakers, we identify two cases:

Speaker B realizes a syntactic dependency that is already part of the tree built by Speaker A. We can distinguish the following 3 subcases:

A.1. Speaker A leaves a syntactic dependency unrealized and Speaker B offers a completion to what Speaker A started, as in (1).

Cuz 31 (Ono & Thompson 1996: 72)
L: his position is pretty uh
A: … % (TSK) (H) stable.
    … yeah

A.2. The same syntactic dependency is realized by both speakers, because Speaker A (at some point) completes what s/he started, possibly after a false start or some planning problems. This case frequently results in overlapping between Speaker A and Speaker B realizing the same slot, and as in (2) and (3).

BOD2018 - KIParla
BO118:	c'è architettu:ra::, c' è:::: [ingegneri~]
		there’s architecture there’s engineer-
BO140: 	[ingegn~ ingegn]eria: sì
		enginee- engeenering yes
BO118: 	si che è [molto buona] anche
		yes which is very good too


BOA3017 - KIParla
BO139 quando si parlano sopra
		when they speak one over the other
devi mettere delle parentesi quadre intorno alle parole
	you have to put square parentheses around words
BO146	ah okay
BO139	che si sovrappongono
	that overlap
BO136	come nei sottotitoli
	like in subtitles
BO139	esatto // infatti io (.) [sto]
	exactly // actually I am
BO147	[>in<fatti te po]tresti fare il sotto~ quello che fa i sotto[titoli]
	actually you could be a subtitler the person who makes subtitles
BO146	[pure te]
	you too
BO145	[sottotitolato]re
	subtitler


A.3.The same syntactic dependency is realized by both speakers, because Speaker A completes their own tree, and Speaker B, in a subsequent turn, selects a syntactic dependency in Speaker’s A tree and realizes it again, either by repeating the content (e.g. for confirmation) or by replacing it (e.g. for correction, as in (5)).

KPS021 - KIParla
PKP126:	quindi l~ la linea tra finzione e realtà
		so the line between fiction and reality
	cioè tra verità non verità non ho ancora capito [dove sta]
	I mean between truth and non-truth I still haven’t understood where it lies
PKP125:	[più tra de]tto e non detto [x]
		more between said and unsaid

The guiding criterion is whether it is possible to apply the ‘if you can link, link’ principle:
if a tree can be linked to a previous tree uttered by a different speaker or by the same speaker but not consecutively, then use the coconstruct relation;
if a tree can be linked to a previous tree uttered by the same speaker consecutively, then merge the trees.
if the intervention by Speaker B is fully overlapping, that is, Speaker B does NOT interrupt Speaker A, then merge and move Speaker B’ unit after (as in (10))

This implies the fact that two dimensions need to be considered: a speaker-dependent one, which only accounts for language uttered by the speaker over time, and a time-dependent one, which accounts for the participation of multiple speakers to the same speech unit.
This is a relatively new aspect for the UD formalism, as written text is usually only concerned with the former perspective.
Eliminating this aspect from the syntactic analysis of spoken language would however introduce a bias in the comparison with planned or written language, as speaker-dependent vision would hide syntactic relations deriving from contributions given by different speakers in the same time frame, and at the same time result in sentence-like units that can only be interpreted (even syntactically) contextually given the contributions of other participants to the interaction.
It is worth remarking that the issue is not entirely new, as for instance social media data might show the same features when it comes to sequences of posts in a thread, possibly posted by different users.

## Backchanneling

Backchannels are short productions uttered by one participant in the conversation when the other participants occupy the floor (back-channel vs front-channel). In order to be recognised as BC, a specific utterance must:
be addressed to the content of the utterance produced by the other speaker
not be required or expected based on previous turn (e.g. answers to questions are expected and required, so they cannot be considered BC, see ex. 3)
not require a reaction from the other speaker (see ex. 1, where the speaker continues)

At their core, these verbal reactions show that the speaker has heard the contribution of the partner, often adding that it has been understood and accepted (see Mereu et al. 2024 and Ward and Tsukahara 2000)

(1) Example of BC - BOA3017, KIParla
BO145:[ma] per[ché mamma c'ha dei <pre]giudizi nei miei confronti> da quando (sono) nata
 but because mum has had some prejudices towards me since I was born
 p[enso]
 I think
BO139: [mhmh]
BO145: e poi daniela non devi avere pregiudizi su di me io <io>
	 and then daniela you musn’t have prejudices about me I

(2) Example of BC - BOD2018, KIParla
BO118: [sì] sì ma anch'io:: però era proprio l'esigenza [de sta da sola
 yes yes me too I also have the need to be alone
 in dei momenti]
 sometimes
BO140: [sì di stare da so:la di non] parla~ di non vedere in faccia [nessuno]
	 yes to be alone not to speak to see nobody’s face
 di:: di stare per::,
 to be

(3) Example of polar reply - BOA3017, KIParla
BO145 [(non) prendi l'insalata?]x@x@
	won’t you have some salad?
BO139	[sì sì]
	yes yes
BO145	[l’ho mangiata tu]tta io
	I have eaten it all myself



BC may have different forms (paraverbal and verbal), such as mh, mhmh, yes, exactly, right.

In dependency view, tokens that form backchannels should be identifiable by an attribute in the misc column (Backchannel=Yes).
In dependency-based view, tokens are linearly placed based on time alignment to their closest token in time, when such information is available. Syntactically, backchannelling enters the syntactic flow and is linked by a discourse relation.
discourse:backchannel is introduced as a new dependency sub-label, but should only be used in the cross-speaker case (i.e. when the backchannel has a different speaker ID to its syntactic parent).

In case of backchannel, we consider that the main speaker keeps the speech turn, its utterance is not interrupted and has not to be segmented. The backchannel will be placed in a separate sentence.

TODO: head selection criteria

TODO: can the backchannel be used to take the floor?

Encoding: In the speaker-based view, the backchannel has a feature:
`Backchannel=<sent-id>::<token-id>`

## Question answering

Spk1: Where do you go?
Spk2: To Bologne.

Spk1: I go to Bologne.
Spk2: When?
Spk1: Next week.

The last example is no very far from a coconstruction such as:
Spk1: I go to Bologne.
Spk2: Tomorrow?
