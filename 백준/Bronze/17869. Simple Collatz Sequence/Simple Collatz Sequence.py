
import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
while True:
    cnt += 1
    if n % 2 == 0:
        n /= 2
    else:
        n += 1

    if n == 1:
        break

print(cnt)
