import sys

y, x = map(int, sys.stdin.readline().strip().split(" "))
g = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(y)]

t = []
for i in range(y-3+1):
    for j in range(x-3+1):
        t += [(i, j, sum(g[i][j:j+3]) + sum(g[i+1][j:j + 3]) + sum(g[i+2][j:j + 3]))]

m_g = max(t, key=lambda x: x[2])
print(m_g[2])
print(m_g[0]+1, m_g[1]+1)
