import sys

temp = "I, O, S, H, Z, X, N".split(", ")
a = sys.stdin.readline().rstrip()

r = "YES"
for i in a:
    if i not in temp:
        r = "NO"
        break
print(r)

