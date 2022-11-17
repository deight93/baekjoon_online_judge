import sys

f = [0] * 1000001
g = [1] * 1000001

for i in range(1, 1000001):
    for j in range(0, 1000001, i):
        f[j] += i

    if i != 1:
        g[i] = g[i - 1] + f[i]


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(g[n])

