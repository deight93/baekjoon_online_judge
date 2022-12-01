
import sys

n, w, h = map(int, sys.stdin.readline().rstrip().split(" "))

for _ in range(n):
    s = int(sys.stdin.readline().rstrip())
    if s <= (w**2+h**2)**0.5:
        print("YES")
    else:
        print("NO")
