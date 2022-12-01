
import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x1, y1, f1, x2, y2, f2 = map(int, sys.stdin.readline().rstrip().split(" "))
    print(abs(x1-x2)+abs(y1-y2)+f1+f2)



