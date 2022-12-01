
import sys

a1, b1, c1, d1 = map(int, sys.stdin.readline().rstrip().split(" "))
a2, b2, c2, d2 = map(int, sys.stdin.readline().rstrip().split(" "))

print(max(abs(min(a1, a2)-max(c1, c2)), abs(min(b1, b2)-max(d1, d2)))**2)


