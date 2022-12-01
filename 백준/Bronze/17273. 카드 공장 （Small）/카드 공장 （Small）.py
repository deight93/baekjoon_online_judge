import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
ab = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
k = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
r_c = [i[0] for i in ab]

for i in k:
    for idx, j in enumerate(r_c):
        if j <= i:
            r_c[idx] = ab[idx][1]
            ab[idx].reverse()
print(sum(r_c))

