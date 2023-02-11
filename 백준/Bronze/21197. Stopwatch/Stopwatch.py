import sys

n = int(sys.stdin.readline().rstrip())
if n % 2 == 1:
    print("still running")
else:
    p = 0
    for _ in range(n//2):
        a = int(sys.stdin.readline().rstrip())
        b = int(sys.stdin.readline().rstrip())
        p += (b - a)
    print(p)
