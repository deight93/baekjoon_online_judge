import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(" ")
    if sorted(a) == sorted(set(b)):
        print("YES")
    else:
        print("NO")

