import sys

x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
t = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    t += (a*b)
if x == t:
    print("Yes")
else:
    print("No")


