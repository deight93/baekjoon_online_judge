import sys

c = int(sys.stdin.readline())

for _ in range(c):
    d, n = map(int, sys.stdin.readline().split())
    p = 0
    a = 0
    count = {0 : 1}
    for s in map(int, sys.stdin.readline().split()):
        p = (p + s) % d

        if p in count:
            a += count[p]
            count[p] += 1
        else:
            count[p] = 1
    print(a)