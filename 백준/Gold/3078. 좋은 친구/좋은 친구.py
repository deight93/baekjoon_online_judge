import sys

n, k = map(int, sys.stdin.readline().split())
nl = [len(sys.stdin.readline().rstrip()) for _ in range(n)]

name_len_cnt = [0] * 21
cnt = 0

for i in range(n-1):
    if i == 0:
        cnt += nl[:k+1].count(nl[0])-1
        for j in nl[:k+1]:
            name_len_cnt[j] += 1
    else:
        if i+k < n:
            name_len_cnt[nl[i+k]] += 1
        a = nl[i]
        b = nl[i-1]
        name_len_cnt[b] -= 1
        cnt += (name_len_cnt[a]-1)
print(cnt)
