import math

from output import print_matrix


g = lambda H: 9.806666 - 0.000003 * H
m = 98000
S = 201
engines = 3
P_f = lambda M: engines * (3390 * M * M - 6921 * M + 33431) #ОК
rho = lambda H: 1.22293 - 0.00011 * H
a = lambda H: 340.28431 - 0.00382 * H
M_f = lambda v, H: v / a(H)
v_f = lambda v1, v2: (v1 + v2) / 2
H_f = lambda H1, H2: (H1 + H2) / 2

Cy0=-0.221
Cyalpha=0.082
Cy = lambda alpha: Cyalpha * alpha + Cy0
#Cx_f = lambda alpha: (lambda cy_a=Cy(alpha): 0.128 * cy_a * cy_a - 0.072 * cy_a + 0.032)()


def Cx_f(alpha):
    cy_a = Cy(alpha)
    return 0.09 * cy_a * cy_a - 0.035 * cy_a + 0.025

qS_f = lambda v, H: rho(H) * v * v / 2 * S
#alpha_f = lambda v, H: (lambda qS=qS_f(v, H): (m * g(H) - Cy0 * qS)/(P_f(M_f(v, H)) / 57.3 + Cyalpha * qS))()

def alpha_f(v, H):
    qS = qS_f(v, H)
    P = P_f(M_f(v, H))
    return (m * g(H) - Cy0 * qS) / (P / 57.3 + Cyalpha * qS)

X_f = lambda Cx, v, H: Cx * qS_f(v, H)
theta_f = lambda P, X, g: (P - X) * 57.3 / (m * g)


def t1(v1, v2, H):
    v = v_f(v1, v2)
    P = P_f(M_f(v, H))
    alpha = alpha_f(v, H)
    Cx = Cx_f(alpha)
    qS = qS_f(v, H)
    X = Cx * qS
    res = m * (v2 - v1) / (P - X)
    return res


def t2(H1, H2, v):
    H = H_f(H1, H2)
    P = P_f(M_f(v, H))
    Cx = Cx_f(alpha_f(v, H))
    X = X_f(Cx, v, H)
    theta = theta_f(P, X, g(H))
    return 57.3 * (H2 - H1) / (v * theta)


def t3(v1, v2, H1, H2):
    v = v_f(v1, v2)
    H = H_f(H1, H2)
    P = P_f(M_f(v, H))
    Cx = Cx_f(alpha_f(v, H))
    X = X_f(Cx, v, H)
    theta = theta_f(P, X, g(H))
    k = (v2 - v1) / (H2 - H1)
    #theta = (lambda P, X, g: (P - X) * 57.3 / (m * (k * v + g)))(P, X, g(H))
    return 1 / (k * theta / 57.3) * math.log(v2 / v1)

def test():
    yield 1
    print(666)


freqH = 10
freqV = 10
fa_H1 = 700
fa_H2 = 9250
fa_v1 = round(350 / 3.6)
fa_v2 = round(980 / 3.6)
dH = (fa_H2 - fa_H1) / freqH
dV = (fa_v2 - fa_v1) / freqV

VM = [[t1(dV * j + fa_v1, dV * (j + 1) + fa_v1, dH * i + fa_H1) for j in range(freqV)] for i in range(freqH + 1)]
HM = [[t2(dH * i + fa_H1, dH * (i + 1) + fa_H1, dV * j + fa_v1) for j in range(freqV + 1)] for i in range(freqH)]
VHM = [[t3(dV * j + fa_v1, dV * (j + 1) + fa_v1, dH * i + fa_H1, dH * (i + 1) + fa_H1) for j in range(freqV)] for i in range(freqH)]

with open("t1.txt", "w") as f:
    print_matrix(VM, f)

#print()

with open("t2.txt", "w") as f:
    print_matrix(HM, f)

#print()

with open("t3.txt", "w") as f:
    print_matrix(VHM, f)

if __name__ == "__main__":
    H = 700
    dV = (980 - 350) / 3.6 / 5
    v1 = 350 / 3.6
    vs = (v1 + v1 + dV) / 2
    rho_value = 1.22293 - 0.00011 * H
    qS = rho_value * vs * vs / 2 * S
    alpha = alpha_f(vs, H)
    Cx = Cx_f(alpha)
    print(f"dV = {dV}")
    print(f"v1 = {v1}")
    print(f"vs = {vs}")
    print(f"rho = {rho_value}")
    print(f"qS = {qS}")
    print(f"alpha = {alpha}")
    print(f"Cx = {Cx}")


#t = test()
#next(t)
#next(t)

#draw_time_matrix(fa_v1, fa_H1, dV, dH, VM, HM, VHM)