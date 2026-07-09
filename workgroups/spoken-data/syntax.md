---
layout: base
title:  'Morphology'
udver: '2'
---

# Syntax

## Co-constructed syntax

We consider as co-constructions those syntactic relations (without any restrictions) that hold between utterances produced (i) by different speakers or (ii) by the same speaker but after an interruption by another speaker. In interactive scenarios, indeed, multiple speakers may intertwine their utterances, sometimes even perfectly overlapping (Lerner 1991, Sacks 1992, Ono & Thompson 1996, Helasvuo 2004, Calabria 2023).

A coconstruction is encoded by a feature on the root of the second utterance indicating the syntactic role of the second utterance towards the first utterance, the sent-id of the first utterance, and the token-id of the governor of the second utterance:

`Coconstruct=<deprel>::<sent-id>::<token-id>`

### Typology of coconstructions

We distinguish three major types of co-constructions:co-construction proper,  wh-question constructions, and backchannelling.

### 1. Coconstruction proper
The key distinction within coconstructions proper concerns whether Speaker 2 realizes a dependency that is already projected by Speaker 1 (case A), or whether Speaker 2 adds a new dependency to the structure initiated by Speaker 1 (case B).

__A. Speaker 2 realizes an already projected dependency.__
When Speaker 2 realizes a dependency projected by Speaker 1, we distinguish three subcases reflecting the status of that dependency at the moment of realization: unrealized, in progress, or already realized.

__A.1 Completion__: Speaker 1 leaves a syntactic dependency unrealized, and Speaker 2 provides the missing material, completing the structure initiated by Speaker 1, as in Example (1).

(1)

__Cuz 31 (Ono & Thompson 1996: 72)__

L: his position is pretty uh

A: … % (TSK) (H) __stable__.
    … yeah

__A.2. Parallel realisation__: the same syntactic dependency is realized by both speakers. Speaker 1 projects and eventually completes the structure, often after hesitation or a false start, while Speaker 2 simultaneously or near-simultaneously fills the same syntactic slot


This case frequently results in overlapping between Speaker A and Speaker B realizing the same slot, and as in (2).

(2)

__BOD2018 - KIParla__

BO118:	c'è architettu:ra::, c' è:::: __[ingegneri~]__

_there’s architecture there’s engineer-_

BO140: 	__[ingegn~ ingegn]eria:__ sì

_enginee- engeenering yes_

BO118: 	si che è [molto buona] anche
_yes which is very good too_

__A.3. Subsequent realisation__: Speaker 1 completes their own tree, and Speaker 2 subsequently selects a dependency in Speaker 1’s structure and realizes it again, either by repeating or replacing material in the same syntactic slot, as in (3) and (4).


(3)

__Rhapsodie - D2001__

$L2 "eh bien" je crois que je ne me suis pas

_well I think I haven't_

$L2 conduit d'une façon conforme à ce qu'on

_behaved as one would_

$L2 attend “euh" { { d’une jeune fille d’abord

_expect from a young girl first_

$L2 | ˆ et d’une femme ensuite } |} //+

_and from a woman afterwards_

$L1 {| d’une jeune bourgeoise |} ?//+

_from a young bourgeois girl?_

$L2 {| “disons" d’une jeune bourgeoise } //

_let's say from a young bourgeois girl_


(4)

__KPS021 - KIParla__

PKP126:	quindi l~ la linea tra finzione e realtà

_so the line between fiction and reality_

cioè tra verità non verità non ho ancora capito [dove sta]

_I mean between truth and non-truth I still haven’t understood where it lies_

PKP125:	[più tra de]tto e non detto [x]

_more between said and unsaid_

__B. Speaker B adds a new dependency__: Speaker 2 realizes a syntactic dependency that is not already projected by Speaker 1, thereby extending the syntactic structure initiated by Speaker 1


(5) 

__Ono and Thompson (1996: 81)__

M: they must know each other.

H: . . . very well.

(6) 

__KIPArla - BOA3017__

BO139: quando si parlano sopra

_when they speak one over the other_

devi mettere delle parentesi quadre

_you have to put square parentheses_

intorno alle parole

_around words_

BO146: ah okay

_oh okay_

BO139: che si sovrappongono

_that overlap_

BO136: come nei sottotitoli

_like in subtitles_

The guiding criterion is whether it is possible to apply the ‘if you can link, link’ principle:
if a tree can be linked to a previous tree uttered by a different speaker or by the same speaker but not consecutively, then use the coconstruct relation;
if a tree can be linked to a previous tree uttered by the same speaker consecutively, then merge the trees.
if the intervention by Speaker 2 is fully overlapping, that is, Speaker 2 does NOT interrupt Speaker 1, then merge and move Speaker 2’ unit after.

This implies the fact that two dimensions need to be considered: a speaker-dependent one, which only accounts for language uttered by the speaker over time, and a time-dependent one, which accounts for the participation of multiple speakers to the same speech unit.
This is a relatively new aspect for the UD formalism, as written text is usually only concerned with the former perspective.
Eliminating this aspect from the syntactic analysis of spoken language would however introduce a bias in the comparison with planned or written language, as speaker-dependent vision would hide syntactic relations deriving from contributions given by different speakers in the same time frame, and at the same time result in sentence-like units that can only be interpreted (even syntactically) contextually given the contributions of other participants to the interaction.
It is worth remarking that the issue is not entirely new, as for instance social media data might show the same features when it comes to sequences of posts in a thread, possibly posted by different users.

### 2. Wh-questions
Answers to wh-questions are analysed as syntactically dependent on the question, and thus as part of the same rectional unit, as already proposed in the guidelines of Rhapsodie.

(7) 

__KIParla - PTA007__

TOR001: dove vai ad arrampicare?

_where do you climb?_

TOI007: al bi side4 vicino alla colletta

_at the bi side close to colletta_

We therefore consider answers to wh-questions as cases of coconstructions, insofar as they realize syntactic material licensed by the interrogative structure of the preceding turn. By contrast, we do not treat answers to polar questions as  coconstructions, since their response items do not depend syntactically on any element of the question nor fill a pre-existing syntactic slot.



### 3. Backchanneling

Backchannels are short productions uttered by one participant in the conversation when the other participants occupy the floor (back-channel vs front-channel). They may be verbal (_yes_) or paraverbal (_mhmh_) and mainly serve to signal attention or alignment. At their core, hese verbal reactions show that the speaker has heard the contribution of the partner, often adding that it has been understood and accepted (see Mereu et al. 2024 and Ward and Tsukahara 2000).

In order to be recognised as BC, a specific utterance must:
- be addressed to the content of the utterance produced by the other speaker
- not be required or expected based on previous turn (e.g. answers to questions are expected and required, so they cannot be considered BC, see ex. 9)
- not require a reaction from the other speaker (see ex. 8, where the speaker continues)


(8) 

__KIParla - BOA3017__

BO145:[ma] per[ché mamma c'ha dei <pre]giudizi nei miei confronti> da quando (sono) nata

_but because mum has had some prejudices towards me since I was born_

p[enso]

_I think_

BO139: [mhmh]

BO145: e poi daniela non devi avere pregiudizi su di me io <io>

_and then daniela you musn’t have prejudices about me I_

(9)

__KIParla - BOD2018__ 

BO118: [sì] sì ma anch'io:: però era proprio l'esigenza [de sta da sola in dei momenti]

_yes yes me too I also have the need to be alone sometimes_

BO140: [__sì__ di stare da so:la di non] parla~ 

_yes to be alone not to talk_





In dependency view, tokens that form backchannels should be identifiable by an attribute in the misc column (Backchannel=Yes).

In dependency-based view, tokens are linearly placed based on time alignment to their closest token in time, when such information is available. Syntactically, backchannelling enters the syntactic flow and is linked by a discourse relation.

discourse:backchannel is introduced as a new dependency sub-label, but should only be used in the cross-speaker case (i.e. when the backchannel has a different speaker ID to its syntactic parent).

In case of backchannel, we consider that the main speaker keeps the speech turn, its utterance is not interrupted and has not to be segmented. The backchannel will be placed in a separate sentence.

TODO: head selection criteria

TODO: can the backchannel be used to take the floor?

Encoding: In the speaker-based view, the backchannel has a feature:
`Backchannel=<sent-id>::<token-id>`
