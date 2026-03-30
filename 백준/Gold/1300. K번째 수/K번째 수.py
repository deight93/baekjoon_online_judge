import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

s, e = 1, k
ans = 0

while s <= e:
    mid = (s+e) // 2

    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)

    if cnt >= k:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
        
print(ans)