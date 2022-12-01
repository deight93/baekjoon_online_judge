import sys

n = int(sys.stdin.readline())

for _ in range(n):
    b = sys.stdin.readline().rstrip()
    print(len(set(b)))