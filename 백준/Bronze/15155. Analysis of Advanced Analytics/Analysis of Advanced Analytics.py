
import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
an = list(map(int, sys.stdin.readline().rstrip().split(" ")))

t = 0
cnt = 1
for a in an:
    t += a
    if t > k:
        cnt += 1
        t = a


print(cnt)


