import numpy as np


def make_eq_terms(x: list, idx: int, n: int, m: int):
    for t in range(n):
        der = x[t] ** idx
        yield [x[t] ** index * der for index in range(m + 1)]


def polyfill(x: list, y: list, m: int):
    n = len(x) #min(len(x), m + 1)
    eq_system = [[sum(coeff_terms) for coeff_terms in zip(*make_eq_terms(x, i, n, m))] for i in range(m + 1)]
    # for row in eq_system:
    #     print()
    #     print(*row)
    #     print()
    A = np.array(eq_system, dtype=float)
    #print(A)
    B = np.fromiter((sum(y[t] * x[t] ** i for t in range(n)) for i in range(m + 1)), dtype=float)
    #B = np.array((sum(y[t] * x[t] ** i for t in range(len(x))) for i in range(m + 1)), dtype=float)
    #print(B)
    R = np.linalg.solve(A, B)
    #with np.printoptions(precision=5, suppress=True):
        #print(R)
    return R


def polyval(poly, x):
    result = 0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result


if __name__ == "__main__":
    #x = [0, 1, 2]
    #y = [0, 1, 4]
    x = [1, 2, 3]
    y = [0.54, -0.416, -0.989]
    polyfill(x, y, 2)