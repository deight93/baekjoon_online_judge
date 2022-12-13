import sys

n = int(sys.stdin.readline().rstrip())
x = int(sys.stdin.readline().rstrip())

total = 0
for i in range(n-1):
    y = int(sys.stdin.readline().rstrip())
    total += (y-x)**2
    x = y
print(total)

