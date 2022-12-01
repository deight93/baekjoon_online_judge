import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

if (n*m) % 3 == 0:
    print("YES")
else:
    print("NO")




