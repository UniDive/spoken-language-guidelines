---
layout: base
title:  'Maximal Unit Segmentation'
udver: '2'
---

- [Maximal Unit Segmentation](#maximal-unit-segmentation)
  - [Speaker view vs. Dependency view](#speaker-view-vs-dependency-view)
  - [What to do](#what-to-do)
    - [Reported speech](#reported-speech)
    - [Adverbial clause without markers](#adverbial-clause-without-markers)
    - [Clause in the paradigm of a dislocated element](#clause-in-the-paradigm-of-a-dislocated-element)
    - [Verbal discourse markers](#verbal-discourse-markers)
    - [Parenthesis](#parenthesis)
    - [False starts](#false-starts)

# Maximal Unit Segmentation

Unlike written text, spoken language unfolds in time and is jointly produced by multiple participants, who continuously cooperate in the real-time production and reception of syntactic structure. Linearized transcriptions, however, necessarily flatten the temporal and multi-party dimension of spoken data.
Universal Dependencies inherits a broadly shared assumption in syntactic theory: that syntax operates within the boundaries of a sentence. While this assumption is largely unproblematic (although, with exceptions) for written language, it raises difficulties for spoken interaction, as syntactic dependencies may extend across speaker turns, interruptions, and overlapping contributions. Existing spoken UD treebanks do not adopt a uniform segmentation strategy, and this makes it difficult to consistently identify what should count as a maximal unit.

Not all currently available spoken treebanks take the same approach at maximal unit segmentation. More specifically, there is a tension between a prosodic and a syntactic view of sentence completion.
The prosodic approach goes for minimal boundaries, segmenting sentences at prosodic termination. The drawback is that these can be hard to find (i.e., subjective interpretation of the annotator, difficult to come up with a clear test), and the resulting unit doesn't always correspond to what we intuitively think of as a sentence.
The syntactic approach can lead to a more "maximal" segmentation. The drawback is that it might lead to arbitrarily long sentences as the boundary between discourse functions and syntactic functions is blended.

Crucially, UD itself never defines what should count as a "sentence": for written language this is rarely an issue, since orthographic and punctuation conventions provide a de facto, if implicit, working definition. For spoken data no such convention exists, and the absence of an explicit notion of sentence becomes a real problem, actively contributing to the lack of a uniform segmentation strategy across existing spoken treebanks. Rather than adopting an arbitrary definition, we need to choose one that keeps spoken data as comparable as possible to the rest of the UD collection.

We suggest to refer to the notion of syntactic **government** when deciding on unit boundaries in spoken data. Government is the relation whereby a governor licenses, and requires the presence of, a dependent, on the basis of its valency: a verb governs its subject and complements, a preposition governs its complement, and so on. Concretely, a governor acts by posing constraints on its dependents' (i) syntactic category, (ii) morphological or syntactic marking, and (iii) linear position. Crucially, government is a purely syntactic relation, orthogonal to prosody, turn-taking, or discourse organization. On this basis, a **rectional unit** is defined as the maximal set of words connected by an uninterrupted chain of government relations, i.e. the largest structure obtainable by tracing every dependent back to its governor, and every governor back to its own governor, until a non-governed root is reached. A rectional unit is therefore not bound by utterance, turn, or speaker boundaries: whenever a dependent's government requirements are satisfied by material produced earlier in the discourse — whether by the same speaker or by a different one — the two belong to the same rectional unit.

The general principle that we want to enforce when dealing with spoken data follows directly from this: **"if you can link, link"**. With respect to syntactic government, this means that whenever a token opens a syntactic slot (as a governor) or fills one (as a dependent), and a suitable governor/dependent can be identified elsewhere in the discourse — even across turns or speakers — the corresponding government-based dependency should be drawn, rather than artificially truncating the tree at a turn or prosodic boundary. Segmentation into maximal units should therefore track the extent of government relations, not the extent of a single speaker's turn.

This distinction has direct consequences on segmentation: it opposes **speaker-dependent maximal units**, bound to a single speaker's turn, to **rectional units**, which are not, and which may accordingly span multiple turns and speakers whenever government relations require it. How this distinction plays out in practice, and how the two kinds of unit relate to one another, is discussed in more detail in the syntax chapter.

In practice, and for the time being, spoken treebanks will be released segmented into **speaker-dependent maximal units** (i.e. one tree per speaker turn) rather than into rectional units. More information on this choice, and on the relation between the speaker-dependent view and the rectional/dependency-based view, is provided in [Speaker view vs. Dependency view](#speaker-view-vs-dependency-view) below.

This means that segmentation has to be performed on the basis of various criteria: syntactic, prosodic and semantic at once.

The "if you can link, link" principle doesn't necessarily need to be applied in a strict way. You may have a discourse marker that is a connective that could technically link back, but shouldn't because there is a very long pause, for example. Language-specific hints that may help us identify the presence of a link.

## Speaker view vs. Dependency view

More specifically, in the speaker-based view each speaker utterance is a new tree, and the Speaker ID attribute applied to the tree (`# speaker_id` metadata). This is the view currently adopted by spoken treebanks in UD, organized in speaker-dependent maximal units.

In the dependency-based view, a tree may be the outcome of multiple speaker concatenations, fully relying on the definition of "sentence" as "rectional unit" and enabling e.g. coconstructions to be realised as regular syntactic dependencies. Each token has a `Speaker_id` attribute in `MISC`, as there may be arbitrarily many speakers contributing.

A conversion script (developed by @bguil) is provided to derive the dependency-based view from the speaker-based view on demand; treebanks are currently released in the speaker-based view only, and parallel releases in both formats are not yet distributed.

## What to do

In writing, juxtaposed clauses are often kept together in a single sentence simply because of the writing system: a comma or a semicolon links them on the page, and this typographical choice, rather than any syntactic requirement, is what makes them stay in one unit. In speech there is no such convention, so we do not have a comparable reason to keep juxtaposed clauses together.

We therefore recommend to cut juxtaposed clauses in different sentences. If you keep them in one sentence for prosodic reasons, use `parataxis`.

But there are some cases with two adjacent clauses where we do not cut, because it is not juxtaposition, as follows:

### Reported speech

When reported speech is introduced by a speech verb (or by any other construction), only the first sentence of the reported speech is attached to it, as the complement of the speech verb, with the relation `ccomp`:

> *she said please don't do that // we need it //*

~~~ sdparse
she said please don't do that
ccomp(said-2, do-5)
~~~

~~~ sdparse
vous étiez là ha ha ha , oh la la !
ccomp(étiez-2, ha-4)
~~~

The root of the reported speech also carries the feature `Reported=Yes`. This feature is needed precisely because reported speech is not always introduced or marked by an explicit construction, so its status cannot always be recovered from the dependency structure alone.

The speech verb can also be inserted inside the reported speech, rather than introducing it:

> *don't do that, she said*
> *ne fais pas ça, a-t-elle dit* (in French, the subject must be inverted)

Such an insertion is usually found at the end of the reported speech, but it can also occur in the middle of it:

> *if you do that, she said, you won't be able to stay*
> *the Christ, Job said/thought, is the Saver*

In these cases the speech verb is not the root of the sentence — it is genuinely inserted — so it is attached with the relation `parataxis:insert`.

~~~ sdparse
don't do that, she said
root(do-2)
parataxis:insert(do-2, said-5)
~~~

### Adverbial clause without markers

In spoken data, markers of subordination (i.e. subordinating conjunctions) are often omitted, since the same relation can be signalled through other strategies instead: grammatical ones (e.g. verbal tense or mood) as well as extragrammatical ones (prosody, non-verbal behaviour, gestures, etc.). In these cases we cannot segment into two sentences, because the subordinate clause is not autonomous: we propose to annotate all such constructions with `advcl`, rather than `parataxis`.

Examples, where subordination is signalled without an explicit subordinating conjunction:

* *j'avais six ans, j'ai eu un accident* — 'I was six, I had an accident' (in French this construction is lexicalized as *il y a*: *il y a six ans* 'six years ago')
* *tu as beau essayer, tu n'y arrives pas* — 'even if you try, you can't do it', lit. 'you have nice try…' (*avoir beau* cannot be used in a main clause: it is a verbal idiom that is lexically subordinated)
* *tu me l'aurais dit, je ne serais pas venu* — 'if you had told me, I wouldn't have come', lit. 'you'd have told me' (here the subordination is marked by the conditional)
* *hai voglia a provarci, non ci riuscirai* — 'you can try, you won't do it', lit. 'you have willingness to try'
* *tu le fais, tu le fais pas, ça revient au même* — 'whether you do it or not, it amounts to the same thing', lit. 'you do it, you don't do it'

See also, for English:

> *It would still give him room to progress in the current job group should he not be promoted.* (`sent_id`: email-enronsent30_01-0047, `document_id`: en_ewt-ud-train)

### Clause in the paradigm of a dislocated element

In some cases, the first of two adjacent clauses is not asserted on its own — the speaker is not really claiming 'I have friends', 'she's someone', or 'there is someone' — but instead functions as a dislocated element that introduces a referent for the second clause. Because the first clause is not autonomous, we cannot segment into two sentences: we propose to annotate these constructions with `dislocated` (or `dislocated:subj`), rather than `parataxis`.

Examples:

* *j'ai des copines, je m'entends super bien avec* — 'I have friends, I get along really well with [them]'
* *c'est quelqu'un, elle est, elle est trop gentille* — 'she's someone, she is, she is so kind'
* *c'è questa non viene mai in palestra* — 'there is this one, she doesn't ever come to the gym'

(See also examples of dislocated units with a verbal head in ParisStories: [universal.grew.fr/?custom=6971f0768e170](https://universal.grew.fr/?custom=6971f0768e170))

An alternative analysis would treat the second clause as a relative clause without an overt relativizer (*j'ai des copines avec qui je m'entends super bien* 'I have friends (who) I get along really well with'), but the prosody argues against this: the prosody of the dislocated construction is instead comparable to that of:

> *mes copines de fac, je m'entends super bien avec* — 'my college friends, I get along really well with [them]'

### Verbal discourse markers

Verbal discourse markers are relevant to this discussion too, since they are clausal in form (e.g. *I mean*, *I guess*, *I know*…). However, they are not autonomous units: they are attached to the clause they accompany with a `discourse` relation.

### Parenthesis

A parenthesis is a clause that could be uttered on its own as a sentence, but is instead inserted inside another sentence. It generally comments on the whole sentence, or on part of it, and is attached with `parataxis:parenth`.

### False starts

A false start is treated as a reparandum whenever it is followed by a repair: since it is not an autonomous unit on its own, it is kept within the same sentence as its repair, linked to it with the relation `reparandum`.

Examples:

* *you you … we have to do that*
* *we should … we must do that*
* *il y a XXX … vous verrez qu'il y a des formes d'art qui ne sont pas le reflet de la société.*
* *j'ai … il se trouve que dans les adresses qu'on m'avait données, j'ai, euh, il y a deux rendez-vous que j'ai dû remettre parce que les gens vendaient, euh, euh, des biens de famille.*

If there is no repair, the false start is instead treated as a separate sentence.

By default, a false start is assumed to be followed by a repair, unless the syntactic structure of the second part is completely unrelated to that of the first — in which case the two are segmented as independent sentences.

NOTE: there are also cases where the main clause is interrupted and the speaker restarts from scratch, rather than repairing the interrupted clause. SST annotates these with `parataxis:restart`; we propose instead to segment the two parts, marking the first one with the feature `Scrap`.

ex. what did you just -- which line will you draw
