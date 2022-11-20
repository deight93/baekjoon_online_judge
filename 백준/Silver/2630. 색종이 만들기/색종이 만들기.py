import sys

n = int(sys.stdin.readline().rstrip())
s = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
r = []


def check_square(x, y, n):
    color = s[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != s[i][j]:
                check_square(x, y, n//2)
                check_square(x, y+n//2, n//2)
                check_square(x+n//2, y, n//2)
                check_square(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        r.append(0)
    else:
        r.append(1)


check_square(0, 0, n)
print(r.count(0))
print(r.count(1))

