import sys

k, d = map(int, sys.stdin.readline().rstrip().split(" "))
b = 2
cnt = 0
while True:
    d -= k * (b ** cnt)

    if d >= 0:
        cnt += 1
    else:
        break

print(cnt)

