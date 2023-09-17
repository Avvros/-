import numpy as np


def make_eq_terms(x: list, idx: int, m: int):
    for t in range(len(x)):
        der = x[t] ** idx
        yield [x[t] ** index * der for index in range(m + 1)]


def polyfill(x: list, y: list, m: int):
    eq_system = [[sum(coeff_terms) for coeff_terms in zip(*make_eq_terms(x, i, m))] for i in range(m + 1)]
    # for row in eq_system:
    #     print()
    #     print(*row)
    #     print()
    A = np.array(eq_system, dtype=float)
    #print(A)
    B = np.fromiter((sum(y[t] * x[t] ** i for t in range(len(x))) for i in range(m + 1)), dtype=float)
    #B = np.array((sum(y[t] * x[t] ** i for t in range(len(x))) for i in range(m + 1)), dtype=float)
    #print(B)
    R = np.linalg.solve(A, B)
    with np.printoptions(precision=3, suppress=True):
        print(R)





#x = [0, 1, 2]
#y = [0, 1, 4]
#polyfill(x, y, 2)


#print()
#load("vals.csv")
