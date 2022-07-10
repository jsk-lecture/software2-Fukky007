not(A-B) :- nand(A,A,B,_).
and(A-B-C) :- nand(A,B,X,_), not(X, C).
or(A-B-C) :- not(A, X), not(B, Y), nand(X,Y,C,_).
    
