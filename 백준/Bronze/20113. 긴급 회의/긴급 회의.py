import sys

n = int(sys.stdin.readline().rstrip())
p = map(int, sys.stdin.readline().rstrip().split(" "))

count_v = [0 for _ in range(n+1)]
for i in p:
    count_v[i] += 1

m = max(count_v[1:])
if count_v[0] == n or count_v[1:].count(m) >= 2:
    print("skipped")
else:
    print(count_v[1:].index(m)+1)