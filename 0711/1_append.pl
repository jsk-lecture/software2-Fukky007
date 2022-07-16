append([], Xs, Xs).
append([X | Ls], Ys, [X | Zs]) :- append(Ls, Ys, Zs).
