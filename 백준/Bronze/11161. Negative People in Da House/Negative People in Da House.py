import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m = int(sys.stdin.readline().rstrip())
    low = 0
    cur = 0
    for _ in range(m):
        p1, p2 = map(int, sys.stdin.readline().rstrip().split(" "))
        cur += p1-p2
        if low > cur:
            low = cur

    print(-1*low)

