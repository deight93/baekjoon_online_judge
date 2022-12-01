
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    print(2**k-1)