import sys

n = int(sys.stdin.readline())
k = 0
cnt = 0
while True:
    k += 1
    if n == 0:
        break
    if n < k:
        k = 1
    n -= k
    cnt += 1

print(cnt)