n, k, p = map(int, input().split())
b = list(map(int, input().split()))

cnt = 0
for i in range(n):
    비정상 = k - sum(b[i*k:(i*k)+k])
    if 비정상 < p:
        cnt += 1
print(cnt)