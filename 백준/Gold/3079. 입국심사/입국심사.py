import sys

n, m = map(int, sys.stdin.readline().split())
tk = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

l = min(tk)
r = max(tk)*m
ans = r

while l <= r:
    total = 0
    mid = (l + r) // 2
    for t in tk:
        total += mid // t
    if total >= m:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1

print(ans)