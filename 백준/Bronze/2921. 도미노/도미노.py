import sys

n = int(sys.stdin.readline())

total = 0
for i in range(n+1):
    for j in range(i, n+1):
        total += i+j

print(total)