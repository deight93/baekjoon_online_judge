import sys

n = int(sys.stdin.readline())
a = n+1
b = n-1

total = 0
for i in range(1, b+1):
    total += a*i
print(total)
