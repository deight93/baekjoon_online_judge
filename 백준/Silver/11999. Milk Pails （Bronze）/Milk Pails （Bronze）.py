
import sys

x, y, m = map(int, sys.stdin.readline().rstrip().split(" "))

max_m = 0
for i in range(1000):
    for j in range(1000):
        if (x*i)+(y*j) <= m:
            max_m = max(max_m, (x*i)+(y*j))

print(max_m)

