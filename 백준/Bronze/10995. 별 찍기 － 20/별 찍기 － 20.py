import sys

n = int(sys.stdin.readline())
a = "* "
b = " *"
t = []
for i in range(1, n+1):
    if i%2 == 1:
        t += [a * n]
    else:
        t += [b * n]

[print(i.rstrip()) for i in t]