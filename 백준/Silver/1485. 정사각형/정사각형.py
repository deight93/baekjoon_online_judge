import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sorted([list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(4)])
    a = ((s[0][0] - s[1][0]) ** 2 + (s[0][1] - s[1][1]) ** 2) ** 0.5
    b = ((s[0][0] - s[2][0]) ** 2 + (s[0][1] - s[2][1]) ** 2) ** 0.5
    c = ((s[3][0] - s[1][0]) ** 2 + (s[3][1] - s[1][1]) ** 2) ** 0.5
    d = ((s[3][0] - s[2][0]) ** 2 + (s[3][1] - s[2][1]) ** 2) ** 0.5
    e = ((s[0][0] - s[3][0]) ** 2 + (s[0][1] - s[3][1]) ** 2) ** 0.5
    f = ((s[1][0] - s[2][0]) ** 2 + (s[1][1] - s[2][1]) ** 2) ** 0.5
    if len({a, b, c, d}) == 1 and len({e, f}) == 1:
        print(1)
    else:
        print(0)