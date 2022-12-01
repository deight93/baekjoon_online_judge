import sys

n = int(sys.stdin.readline().rstrip())
n_list = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 1
for i in range(1, n):
    if n_list[i] != n_list[i-1]:
        cnt += 1
print(cnt+1)


