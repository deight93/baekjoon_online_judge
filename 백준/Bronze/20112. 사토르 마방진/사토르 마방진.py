import sys

n = int(sys.stdin.readline().rstrip())
w = [sys.stdin.readline().rstrip() for _ in range(n)]
zip_w = list(zip(*w))

p = "YES"
for i in range(n):
    if w[i] != "".join(zip_w[i]):
        p = "NO"
        break
print(p)