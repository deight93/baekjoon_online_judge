
import sys

n = int(sys.stdin.readline().rstrip())
b = [[int(j) for j in sys.stdin.readline().split(" ")] for _ in range(n)]
b2 = [list(i) for i in zip(*b)]

t = [0 for _ in range(n)]
for i in b2:
    for j in range(n):
        if i.count(i[j]) != 1:
            t[j] += 0
        else:
            t[j] += i[j]
for k in t:
    print(k)

