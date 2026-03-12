n, k = map(int, input().split())
b = n - (k+1) * k // 2

if b < 0:
    print(-1)
else:
    if b % k == 0:
        print(k-1)
    else:
        print(k)