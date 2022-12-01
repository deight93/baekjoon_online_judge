
import sys

n = int(sys.stdin.readline().rstrip())
p = sorted([float(sys.stdin.readline().rstrip()) for _ in range(n)])
print("{:.2f}".format(p[1]))
