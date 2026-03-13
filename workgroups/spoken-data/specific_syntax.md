---
layout: base
title:  'Other Constructions'
udver: '2'
---

# Other Constructions

This section of the [syntax overview](syntax.html) contains detailed discussion of particular linguistic constructions that fall outside (or cut across) the main categories of simple clauses, complex clauses, and nominal phrases.

* [Paratactic constructions](#paratactic-constructions)
* [Punctuation](#punctuation)

#TODO: revise for speech

## Paratactic Constructions

The [parataxis]() relation is used to analyze a number of constructions where clauses are combined
by relations that are looser than standard coordination.

### Side-by-side sentences ("run-on sentences")

The [parataxis]() relation is used for a pair of what could have been standalone sentences,
but which are being treated together as a single sentence. This may happen because sentence
segmentation of the sentence was done primarily following the presence of sentence-final punctuation,
and these clauses are joined by punctuation such as a colon or comma, or not delimited by punctuation
at all. In a spoken corpus, it may happen because what is labeled as a sentence is more
commonly an utterance turn. Even if the treebanker is doing the sentence division, it may
happen because there seems to be a clear discourse relation linking two clauses.
Sometimes there are more than two sentences joined in this way. In this case we make all the later sentences
dependents of the first one, to maximize similarity to the analysis used for conjunction.

~~~ sdparse
Bearded dragons are sight hunters , they need to see the food to move .
parataxis(hunters, need)
~~~

This relation may happen with units that are smaller than sentences:

~~~ sdparse
Divided world the CIA
amod(world, Divided)
parataxis(world, CIA)
det(CIA, the)
~~~

### Paired clauses with non-conjunction connective ("X so Y" etc.)

The relation is also used for clauses connected by a word like *so*, *then*, *therefore*, or *however*
if neither clause is interpreted as modifying the other, and there is no coordinating conjunction:

~~~ sdparse
He claimed to be a wizard ; however/ADV , he turned out to be a humbug .
parataxis(claimed, turned)
advmod(turned, however)
~~~

~~~ sdparse
I 'm hungry , so/ADV I 'm getting a bagel .
parataxis(hungry, getting)
advmod(getting, so)
~~~

The following, by contrast, are [advcl]() modifiers:

~~~ sdparse
Eat now so/ADV you wo n't be hungry later .
advcl(Eat, hungry)
advmod(hungry, so)
~~~

~~~ sdparse
If/SCONJ you build it , then/ADV they will come .
advcl(come, build)
mark(build, If)
advmod(come, then)
~~~

Note that *if*-clauses should almost always be analyzed as subordinate, even when *then* is present.

### Reported speech

When a speech verb interrupts reported speech content, the interruption is treated as a parenthetical parataxis:

~~~ sdparse
The guy , John said , left early in the morning
parataxis(left, said)
punct(said, ,-3)
punct(said, ,-6)
~~~

See further discussion of reported speech at [ccomp](/u/dep/ccomp.html#reported-speech).

### News article bylines

We have used the parataxis relation to connect the parts of a news article byline.
There does not seem to be a better relation to use.

~~~ sdparse
Washington ( CNN ) :
parataxis(Washington, CNN)
punct(CNN, ()
punct(CNN, ))
punct(CNN, :)
~~~

### Interjected Clauses

Single word or phrase interjections are analyzed as [discourse](), but when a whole clause is interjected, we use the relation parataxis.

~~~ sdparse
Calafia has great fries ( they are to die for ! )
parataxis(has, are)
punct(are, ()
punct(are, ))
~~~

~~~ sdparse
Just to let you all know Matt has confirmed the booking for 3rd Dec is OK .
parataxis(confirmed, let)
~~~

In the second example, we treat the second half as the head of the dependency
because the first half feels like a whole clause interjection, not like the main clause of the utterance.

### Tag questions

We also use the parataxis relation for tag questions such as _isn't it?_ or _haven't you?_.

~~~ sdparse
It 's not me , is it ?
parataxis(me, is)
punct(is, ,)
~~~

### Feedback words

In a sentence starting with a feedback word such as _yes_ or _no_ and continuing with a main clause, we take the predicate of the main clause to be the root of the sentence and attach the feedback word to this predicate with a [discourse]() relation:

~~~ sdparse
yes , we should apply for membership .
discourse(apply, yes)
~~~

However, when the feedback is expressed by a full clause instead of a feedback word, the predicate of this clause is taken as the root and the predicate of the following clause is attached with a [parataxis]() relation:

~~~ sdparse
I agree , we should apply for membership .
parataxis(agree, apply)
~~~

## Punctuation

Tokens with the relation [u-dep/punct]() always attach to content words (except in cases of ellipsis) and can never have dependents. Since `punct` is not a normal dependency relation, the usual criteria for determining the head word do not apply.
Instead, we use the following principles:

1. A punctuation mark separating coordinated units is attached to the immediately following conjunct.
2. A punctuation mark preceding or following a dependent unit is attached to that unit.
3. Within the relevant unit, a punctuation mark is attached at the highest possible node that preserves projectivity.
4. Paired punctuation marks (quotes and brackets) should be attached to the same word unless that would create non-projectivity. This word is usually the head of the phrase enclosed in the paired punctuation.

<div id="punct1" class="sd-parse">
We have apples , pears , oranges , and bananas .
obj(have, apples)
conj(apples, pears)
conj(apples, oranges)
conj(apples, bananas)
cc(bananas, and)
punct(pears, ,-4)
punct(oranges, ,-6)
punct(bananas, ,-8)
</div>

<div id="punct2" class="sd-parse">
Der Mann , den Sie gestern kennengelernt haben , kam wieder .
punct(kennengelernt, ,-3)
punct(kennengelernt, ,-9)
punct(kam, .)
</div>

<div id="punct3" class="sd-parse">
A.K.A. , AKA , or a\/k\/a may refer to : “ Also known as ” , used to introduce pseudonyms , aliases , etc. ( Compare f.k.a. for “ formerly known as ” . )
punct(AKA, ,-2)
punct(a/k/a, ,-4)
punct(refer, :)
punct(known-13, “-11)
punct(known-13, ”-15)
punct(used, ,-16)
punct(aliases, ,-21)
punct(etc., ,-23)
punct(Compare, (-25)
punct(Compare, )-35)
punct(known-31, “-29)
punct(known-31, ”-33)
punct(Compare, .-34)
</div>

See also examples at [parataxis]().

## Discourse relations

@andidyer