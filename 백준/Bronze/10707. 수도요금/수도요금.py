import sys

a = [int(sys.stdin.readline().rstrip()) for _ in range(5)]

x = a[0]*a[4]
if a[4] > a[2]:
    y = a[1]+a[3]*(a[4]-a[2])
else:
    y = a[1]

print(min(x, y))