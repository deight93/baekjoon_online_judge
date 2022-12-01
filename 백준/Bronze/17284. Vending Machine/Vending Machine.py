import sys

p = {1: 500, 2: 800, 3: 1000}
b = map(int, sys.stdin.readline().rstrip().split(" "))

t = 5000
for i in b:
    t -= p[i]
print(t)


