
import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
n = int(sys.stdin.readline().rstrip())
j_list = [abs(int(sys.stdin.readline().rstrip())-b) for _ in range(n)]

t = 0
if abs(a-b) > min(j_list):
    t += (1+min(j_list))
else:
    t = abs(a-b)

print(t)
