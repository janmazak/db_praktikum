nv(I, P, K, Od, A, M) :- navstivil(I, P, K, Od), vypil(I, A, M).

nelojalny(P, K) :- nv(_, P, K, Od, A, _), nv(_, P, K2, Od2, A, _), K \= K2, Od2 > Od.
answer_a(P, K) :- nv(_, P, K, _, _, _), \+ nelojalny(P, K).

pil(I, A) :- vypil(I, A, _).
zle(P, A) :- navstivil(I, P, K, _), capuje(K, A, _), \+ pil(I, A).
zle(P, A) :- nv(_, P, _, Od1, A, M1), nv(_, P, _, Od2, A, M2), Od1 < Od2, M1 > M2.
answer_b(P, A) :- nv(_, P, _, _, A, _), \+ zle(P, A).

porazil(P, A, K, I) :- nv(_, P, K, _, A, M), nv(I, P2, K, _, A, M2), P2 \= P, M > M2.
failed(P, A) :- capuje(K, A, _), lubi(P, A), nv(I, P2, K, _, A, _), P2 \= P, \+ porazil(P, A, K, I).
answer_c(P, A) :- lubi(P, A), \+ failed(P, A).

nie_drzgros(P) :- nv(_, P, _, _, A, _), \+ lubi(P, A).
nie_drzgros(P) :- nv(_, P, K, _, A, _), capuje(K, A, C), capuje(K, _, C2), C2 < C.
nie_drzgros(P) :- nv(_, P, K, Od, A, _), capuje(K, A, C), capuje(K2, A, C2), C2 < C, navstivil(_, P, K2, Od2), Od2 < Od.
answer_d(P) :- navstivil(_, P, _, _), \+ nie_drzgros(P).
