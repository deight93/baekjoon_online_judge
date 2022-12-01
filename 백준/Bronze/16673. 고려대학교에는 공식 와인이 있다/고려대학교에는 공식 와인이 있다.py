
import sys

c, k, p = map(int, sys.stdin.readline().rstrip().split(" "))

t = 0
for n in range(1, c+1):
    t += (k*n)+(p*(n**2))

print(t)

