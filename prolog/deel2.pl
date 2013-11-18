/*  Prolog natural_language
 *
 *  Maico Timmerman
 *  CKNUM:   10542590
 */


:-  op( 100, xfy, and).
:-  op( 150, xfy, =>).

% het opvangen van niet gebruikte singletons in statements.
:- style_check(-singleton).

% zin(S) bestaat uit zelfst. naamwoord(X,P,S)+ werkwoordzin(X,P)
sentence( S)  -->
  noun_phrase( X, P, S), verb_phrase( X, P).

% zelfst. naamwoord(X,P,S) bestaat uit lidwoord(X,P12,P,S), zelfst. naamwoord(X,P1)
% en bijvoegelijke bijzin(X,P1,P12) met check dat X geen atoom is, anders moet noun_phrase(X,P,P)
% worden aangeroepen.
noun_phrase( X, P, S)  -->
  determiner( X, P12, P, S), noun( X, P1), rel_clause( X, P1, P12), { \+ atom(X)}.

% zelfst. naamwoord(X,P,P) bestaat uit zelfst. naamwoord(X)
noun_phrase( X, P, P)  -->
  proper_noun( X).

% werkwoord(X,P) bestaat uit werkwoord(X,Y,P1) en zelfst. naamwoord(Y,P1,P)
verb_phrase( X, P)  -->
  trans_verb( X, Y, P1), noun_phrase( Y, P1, P).

% werkwoord (X,P) bestaat uit werkwoord(X,P)
verb_phrase( X, P)  -->
  intrans_verb( X, P).

% bijvoegelijke bijzin (X,P1, P1 en P2) bestaat uit 'that' + werkwoord(X,P2)
rel_clause( X, P1, P1 and P2)  -->
  [that], verb_phrase( X, P2).

% bijvoegelijke bijzin(X,P1,P1) bestaat uit een lege array
rel_clause( X, P1, P1)  --> [].

% lidwoord[de, het, een, mijn, elke] (X,P1,P,alle gevallen(X,P1=>P)) bestaat uit [every]
determiner( X, P1, P, all( X, P1 => P))  --> [every].

% lidwoord waarin (X,P1,P bestaat(X +P1 en P) bestaat uit [a]
determiner( X, P1, P, exists( X, P1 and P)) --> [a].

% zelfst. naamwoord voor iedere man(John en monet)
noun( X, man(X))  -->  [man].
% zelfst. naamwoord voor iedere vrouw(annie)
noun( X, woman(X))  -->  [woman].
% voorbeeld naam voor man
proper_noun( john)  -->  [john].
% voorbeeld naam voor vrouw
proper_noun( annie)  -->  [annie].
% franse impressionistisch schilder leefde rond de 19e eeuw
proper_noun( monet)  -->  [monet].

% 2-delig werkwoord
% iets(X) iets(Y), likes(X,Y) betekent [likes] in array proppen
trans_verb( X, Y, likes( X, Y))  -->  [ likes].

% 2-delig werkwoord
% iets(X) iets(Y), admires(X,Y) betekent [admires] in array proppen
trans_verb( X, Y, admires( X, Y))  -->  [admires].

% simpel werkwoord
% iets(X), paints(X) betekent [paints] in array proppen
intrans_verb( X, paints(X))  -->  [paints].


% Some tests
test1( M)  :-
  sentence( M, [john,paints],[]).

test2( M)  :-
  sentence( M, [a, man, paints], []).

test3( M)  :-
  sentence( M, [every,man,that,paints,admires,monet],[]).

test4( M)  :-
  sentence( M, [annie,admires,every,man,that,paints],[]).

test5( M)  :-
  sentence( M, [every,woman,that,admires,a,man,that,paints,likes,monet],[]).
