import locale

import matplotlib.pyplot as plt
import numpy as np
import times


def read(filename: str):
    with open(filename, "r") as f:
        return [[locale.atof(item) for item in line.split()] for line in f]


t1, t2, t3 = map(read, ("t1.txt", "t2.txt", "t3.txt"))
n = len(t3) + 1
r = [[(0, 0) for i in range(n)] for j in range(n)]
for i in range(n - 2, -1, -1):
    r[n - 1][i] = (r[n - 1][i + 1][0] + t1[n - 1][i], 1)
    r[i][n - 1] = (r[i + 1][n - 1][0] + t2[i][n - 1], 2)
for i in range(n - 2, -1, -1):
    for j in range(n - 2, -1, -1):
        r1 = r[i][j + 1][0]
        r2 = r[i + 1][j][0]
        r3 = r[i + 1][j + 1][0]
        tt1 = t1[i][j]
        tt2 = t2[i][j]
        tt3 = t3[i][j]
        r[i][j] = min((tt1 + r1, 1), (tt2 + r2, 2), (tt3 + r3, 3))

ll = (0, 0)
way = [ll]
while True:
    rv = r[ll[0]][ll[1]]
    if rv[1] <= 0:
        break
    ll = (ll[0] + rv[1] // 2, ll[1] + rv[1] % 2)
    way.append(ll)


time = r[0][0][0]

way = list(zip(*way))

fig, ax = plt.subplots()
#x = way[1] * times.dV + times.fa_v1
dV = times.dV
fa_v1 = times.fa_v1
x = [w1 * dV + fa_v1 for w1 in way[1]]
#y = way[0] * times.dH + times.fa_H1
dH = times.dH
fa_H1 = times.fa_H1
y = [w0 * dH + fa_H1 for w0 in way[0]]
ax.plot(x, y)
ax.set_xticks(np.arange(0, n) * times.dV + times.fa_v1)
ax.set_yticks(np.arange(0, n) * times.dH + times.fa_H1)
plt.grid(visible=True)
plt.show()


print(*reversed(r), sep='\n')
print()
print(*way)
print(time)