import sys

N, R, C = map(int, sys.stdin.readline().split())

result = 0
dr = (0, 0, 1, 1)
dc = (0, 1, 0, 1)

def recursion(n, r, c):
    global result
    if r == R and c == C:
        print(result)
        return

    if not(r <= R < r + n and c <= C < c + n):
        result += n * n
        return

    n //= 2
    for i in range(4):
        nr = r + n * dr[i]
        nc = c + n * dc[i]
        recursion(n, nr, nc)

recursion(2 ** N, 0, 0)