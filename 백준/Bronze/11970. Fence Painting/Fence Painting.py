import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
c, d = map(int, sys.stdin.readline().rstrip().split(" "))

fence = [0 for _ in range(101)]

for i in range(a, b):
    fence[i] = 1

for i in range(c, d):
    fence[i] = 1

print(fence.count(1))


