import sys

n = int(sys.stdin.readline().rstrip())
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
r = "NO"

if sorted(a) == sorted(b):
    if a[0] == b[0] and a[-1] == b[-1]:
        for i in ['a', 'e', 'i', 'o', 'u']:
            a = a.replace(i, "")
            b = b.replace(i, "")
        if a == b:
            r = "YES"
print(r)
