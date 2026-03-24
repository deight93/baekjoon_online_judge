import sys

n, d, k, c = map(int, sys.stdin.readline().split())
cb = [int(sys.stdin.readline()) for _ in range(n)]
cb = cb + cb[:k-1]
cb_cnt = {}

for i in cb[:k]:
    if i in cb_cnt:
        cb_cnt[i] += 1
    else:
        cb_cnt[i] = 1

if c in cb_cnt:
    cnt = len(cb_cnt)
else:
    cnt = len(cb_cnt) + 1


for i in range(1, n):
    cb_cnt[cb[i-1]] -= 1
    if cb_cnt[cb[i-1]] == 0:
        del cb_cnt[cb[i-1]]

    aa = cb_cnt.get(cb[i+k-1], 0)
    cb_cnt[cb[i+k-1]] = aa + 1
    bb = cb_cnt.get(c, 0)

    if bb == 0:
        cnt = max(cnt, len(cb_cnt) + 1)
    else:
        cnt = max(cnt, len(cb_cnt))

print(cnt)