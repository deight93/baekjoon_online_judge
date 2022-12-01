import sys

n = int(sys.stdin.readline().rstrip())
m, k = map(int, sys.stdin.readline().rstrip().split(" "))
a = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))),reverse=True)

total = 0
r_v = "STRESS"
for idx, v in enumerate(a):
    total += v
    if total >= m*k:
        r_v = idx+1
        break
print(r_v)