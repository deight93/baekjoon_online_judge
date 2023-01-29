import sys

n = int(sys.stdin.readline().rstrip())
w = [sys.stdin.readline().rstrip()[::-1] for i in range(n)]
print(" ".join(sorted(w)))