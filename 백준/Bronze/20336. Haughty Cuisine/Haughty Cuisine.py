import sys

n = int(sys.stdin.readline().rstrip())
set_m = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

for i in set_m[0]:
    print(i)
