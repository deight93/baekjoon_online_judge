import sys

w = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
t = 0
for i in range(n):
    wi, li = map(int, sys.stdin.readline().rstrip().split(" "))
    t += wi*li

print(int(t/w))
