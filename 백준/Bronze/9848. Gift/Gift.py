import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
init_t = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(n-1):
    t = int(sys.stdin.readline().rstrip())
    if init_t-t >= k:
        cnt += 1
    init_t = t
print(cnt)

