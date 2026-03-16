n = int(input())

mb = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if b > a:
        mb = min(mb, b)

if mb == 1001:
    print(-1)
else:
    print(mb)