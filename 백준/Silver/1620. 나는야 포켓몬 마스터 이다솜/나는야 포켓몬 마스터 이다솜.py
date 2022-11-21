import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
p_d = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isalpha():
        print(p_d.index(q)+1)
    else:
        print(p_d[int(q)-1])


