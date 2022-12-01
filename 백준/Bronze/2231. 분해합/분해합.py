import sys

n = int(sys.stdin.readline())

n_len = len(str(n-1))
if n_len == 1:
    temp = [str(i) for i in range(1, n+1)]
else:
    temp = [str(i) for i in range(n-n_len*9, n) if i > 0]

ck = True
for i in temp:
    a = 0
    for j in i:
        a += int(j)
    a += int(i)

    if a == n:
        print(i)
        ck = False
        break

if ck is True:
    print(0)