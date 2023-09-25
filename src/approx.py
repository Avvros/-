import numpy as np


def polyfill(x: list, y: list, m: int):
    """
    Аппроксимирует зависимость между множествами x и y к полиному степени m
    :return: массив NumPy вида [b0, b1, ... bm], соответствующий полиному :raw-html:`<br />` b0 + b1 * x + ... + bm * x ^ m
    """
    #eq_system = [[sum(coeff_terms) for coeff_terms in zip(*make_eq_terms(x, i, m))] for i in range(m + 1)]
    eq_system = [[sum(x[t] ** (i + j) for t in range(len(x))) for j in range(m + 1)] for i in range(m + 1)]
    A = np.array(eq_system, dtype=float)
    B = np.fromiter((sum(y[t] * x[t] ** i for t in range(len(x))) for i in range(m + 1)), dtype=float)
    R = np.linalg.solve(A, B)
    return R


def polyval(poly, x):
    result = 0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result


if __name__ == "__main__":
    #x = [0, 1, 2]
    #y = [0, 1, 4]
    #x = [1, 2, 3]
    #y = [0.54, -0.416, -0.989]
    x = [-2, 0, 1]
    y = [6, 4, 9]
    with np.printoptions(precision=5, suppress=True):
        print(polyfill(x, y, 2))