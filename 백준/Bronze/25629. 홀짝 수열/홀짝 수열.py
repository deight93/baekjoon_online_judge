import sys

n = int(sys.stdin.readline().rstrip())
an = map(int, sys.stdin.readline().rstrip().split(" "))
o_n = []
e_n = []

for i in an:
    if i % 2 == 0:
        e_n.append(i)
    else:
        o_n.append(i)


if n % 2 == 1:
    if len(o_n) == n // 2 + 1 and len(e_n) == n // 2:
        print(1)
    else:
        print(0)
else:
    if len(o_n) == n // 2 and len(e_n) == n // 2:
        print(1)
    else:
        print(0)

