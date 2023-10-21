import math
g = lambda H: 9.806666 - 0.000003 * H
m = 98000
S = 201
P_f = lambda M: 2.72 * M * M - 4.95 * M + 32.24
rho = lambda H: 1.22293 - 0.00011 * H
a = lambda H: 340.28431 - 0.00382 * H
M_f = lambda v, H: v / a(H)
v_f = lambda v1, v2: (v1 + v2) / 2
H_f = lambda H1, H2: (H1 + H2) / 2

Cy0=-0.221
Cyalpha=0.082
Cy = lambda alpha: Cyalpha * alpha + Cy0
Cx_f = lambda alpha: (lambda cy_a=Cy(alpha): 0.128 * cy_a * cy_a - 0.072 * cy_a + 0.032)()

qS_f = lambda v, H: rho(H) * v * v / 2 * S
alpha_f = lambda v, H: (lambda qS=qS_f(v, H): (m * g(H) - Cy0 * qS)/(P_f(M_f(v, H)) / 57.3 + Cyalpha * qS))()
X_f = lambda Cx, v, H: Cx * qS_f(v, H)
theta_f = lambda P, X, g: (P - X) * 57.3 / (m * g)

def t1(v1, v2, H):
    v = v_f(v1, v2)
    P = P_f(M_f(v, H))
    Cx = Cx_f(alpha_f(v, H))
    qS = qS_f(v, H)
    return m * (v2 - v1) / (P - Cx * qS)


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
    return 1 / (k * theta) * math.log(v2 / v1)
