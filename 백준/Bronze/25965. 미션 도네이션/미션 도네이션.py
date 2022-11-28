import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    mkda = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]
    k, d, a = map(int, sys.stdin.readline().rstrip().split(" "))
    p = 0
    for j in mkda:
        if (j[0]*k) - (j[1]*d) + (j[2]*a) < 0:
            pass
        else:
            p = p + (j[0]*k) - (j[1]*d) + (j[2]*a)
    print(p)



