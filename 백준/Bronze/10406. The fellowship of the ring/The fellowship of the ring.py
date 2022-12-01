

import sys

w, n, p = map(int, sys.stdin.readline().rstrip().split(" "))
p_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

cnt = 0
for c in p_list:
    if w <= c <= n:
        cnt += 1

print(cnt)
