import sys

h = {}
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    c = sys.stdin.readline().rstrip().split(" ")
    if c[0] in h.keys():
        h[c[0]] += int(c[1])
    else:
        h[c[0]] = int(c[1])

p = "NO"
for k, v in h.items():
    if v == 5:
        p = "YES"
        break
print(p)