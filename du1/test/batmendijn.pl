zradil(P, K) :- navstivil(I1, P, K, O1), vypil(I1, A, _), navstivil(I2, P, K2, O2), vypil(I2, A, _),\+ K = K2, O2 > O1.
answer_a(P, K) :- navstivil(I, P, K, _), vypil(I, _, _), \+ zradil(P, K).

vypil_pri_navsteve(I, A) :- vypil(I, A, _).
odolal(P, A) :- navstivil(I, P, K, _), capuje(K, A, _), \+ vypil_pri_navsteve(I, A).
zmiernil(P, A) :- navstivil(I1, P, _, O1), vypil(I1, A, M1), navstivil(I2, P, _, O2), vypil(I2, A, M2), O2 > O1, M2 < M1.
answer_b(P, A) :- navstivil(I, P, _, _), vypil(I, A, _), \+ odolal(P, A), \+ zmiernil(P, A).


porazil(P, K, A, M) :- navstivil(I2, P, K, _), vypil(I2, A, M2), vypil(_, A, M), M2 > M.
nesampion(P, A) :- lubi(P, A), navstivil(I, P2, K, _), vypil(I, A, M), \+ porazil(P, K, A, M), \+ P = P2.
nesampion(P, A) :- lubi(P, A), capuje(K, A, _), \+ vypil_v_krcme(P, K, A).
vypil_v_krcme(P, K, A) :- navstivil(I, P, K, _), vypil(I, A, _).
answer_c(P, A) :- lubi(P, A), \+ nesampion(P, A).


pil_drahy_alkohol(P) :- navstivil(I, P, K, _), vypil(I, A, _), capuje(K, A, C1), capuje(K, A2, C2), C2 < C1, \+ A2 = A.
pil_neoblubeny_alkohol(P) :- navstivil(I, P, _, _), vypil(I, A, _), \+ lubi(P, A).
pil_nevyhodne_alkohol(P) :- navstivil(_, P, K1, O1), capuje(K1, A, C1), navstivil(I, P, K2, O2), vypil(I, A, _), capuje(K2, A, C2), C2 > C1, O2 > O1.
answer_d(P) :- navstivil(_, P, _, _), \+ pil_drahy_alkohol(P), \+ pil_neoblubeny_alkohol(P), \+ pil_nevyhodne_alkohol(P).