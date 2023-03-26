
import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))
p = list(map(int, sys.stdin.readline().strip().split(" ")))
max_p = 0

for i in range(1, n+1):
    if max_p < p.count(i):
        max_p = p.count(i)
print(max_p)