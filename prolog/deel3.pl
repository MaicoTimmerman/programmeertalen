/*  Prolog natural_language
 *
 *  Maico Timmerman
 *  CKNUM:   10542590
 *  
 *  Definite clause grammar for simple sentences.
 *  if-then, and, or extensions to sentences supported.
 */


:- op(100, xfy, and).
:- op(120, xfy, or).
:- op(150, xfy, =>).

% Catching unused singletons from causing a warning while compiling.
:- style_check(-singleton).


% Normal sentence without any special extensions.
sentence( S) -->  simple_sentence(S).
% 'and' sentence made of a simple sentence and an follow up recursive part. 
sentence( S and S2) --> simple_sentence(S), [and], sentence(S2).
% 'or' sentence made of a simple sentence and an follow up recursive part. 
sentence( S or S2) --> simple_sentence(S), [or], sentence(S2).
% 'if ... then ...' sentence made of a simple sentence and an follow up recursive part. 
sentence( S => S2) --> [if], simple_sentence(S), [then], sentence(S2).

% a sentence build from a noun- and verb-phrase
simple_sentence( S)  --> noun_phrase( X, P, S), verb_phrase( X, P).

% noun_phrase existing of a determiner, a noun, and a relative clause. this rule contains an additional
% condition that checks if the noun is not an atom, but an variable.
% If no check is set then wrong nouns can end up while rebuilding the sentence from a logical expression.
noun_phrase( X, P, S)  --> determiner( X, P12, P, S), noun( X, P1), rel_clause( X, P1, P12), { \+ atom(X)}.
%noun phrase existing of a noun.
noun_phrase( X, P, P)  --> proper_noun( X).

% verb phrase existing of a verb and a noun phrase.
verb_phrase( X, P)  --> trans_verb( X, Y, P1), noun_phrase( Y, P1, P).
% verb phrase existing of only a verb.
verb_phrase( X, P)  --> intrans_verb( X, P).

% a relative clause existing of 'that' and a verb phrase.
rel_clause( X, P1, P1 and P2)  --> [that], verb_phrase( X, P2).
% an empty relative clause. 
rel_clause( X, P1, P1)  --> [].


% determiner for all/every translates to 'every'.
determiner( X, P1, P, all( X, P1 => P))  --> [every].
% determiner for exists/there is translates to 'a'
determiner( X, P1, P, exists( X, P1 and P)) --> [a].

% noun for all man.
noun( X, man(X))  -->  [man].
% noun for all women.
noun( X, woman(X))  -->  [woman].

% example names for testing purposes.
proper_noun( john)  -->  [john].
proper_noun( annie)  -->  [annie].
proper_noun( monet)  -->  [monet].

% transitive verbs:
trans_verb( X, Y, likes( X, Y))  -->  [ likes].
trans_verb( X, Y, admires( X, Y))  -->  [admires].

% intrasitive verbs:
intrans_verb( X, paints(X))  -->  [paints].


% Some tests:
test1( M) :-
    sentence( M, [john,paints],[]).
test2( M) :-
    sentence( M, [a, man, paints], []).
test3( M) :-
    sentence( M, [every,man,that,paints,admires,monet],[]).
test4( M) :-
    sentence( M, [annie,admires,every,man,that,paints],[]).
test5( M) :-
    sentence( M, [every,woman,that,admires,a,man,that,paints,likes,monet],[]).
test6( M) :-
    sentence( M, [a, man, paints, and, john, paints],[]).
test7( M) :-
    sentence( M, [a, man, paints, or, john, paints],[]).
test8( M) :-
    sentence( M, [if, a, man, paints, then, every, woman, paints],[]).
