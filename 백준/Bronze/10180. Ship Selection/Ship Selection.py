
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, d = map(int, sys.stdin.readline().rstrip().split(" "))
    cnt = 0
    for i in range(n):
        v, f, c = map(int, sys.stdin.readline().rstrip().split(" "))
        if f >= c*(d/v):
            cnt += 1
    print(cnt)




