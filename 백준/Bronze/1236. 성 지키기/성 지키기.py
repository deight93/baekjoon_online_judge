import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
v_c = [sys.stdin.readline().rstrip() for _ in range(n)]
h_c = list(map(list, zip(*v_c)))
v_g = 0
h_g = 0
for c in v_c:
    if "X" not in c:
        v_g += 1

for c in h_c:
    if "X" not in c:
        h_g += 1

print(max(h_g, v_g))


