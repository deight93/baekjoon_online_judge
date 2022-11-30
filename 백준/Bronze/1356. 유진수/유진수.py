
import sys

n = sys.stdin.readline().rstrip()

ck = False
for i in range(1, len(n)):
    a1 = 1
    for j in n[:i]:
        a1 *= int(j)

    a2 = 1
    for j in n[i:]:
        a2 *= int(j)

    if a1 == a2:
        ck = True
        break

if ck is True:
    print('YES')
else:
    print('NO')
