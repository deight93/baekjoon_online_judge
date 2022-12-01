import sys

n = sys.stdin.readline().rstrip()

cnt = 0
while True:
    if len(n) == 1:
        break

    a = 1
    for i in n:
        a *= int(i)
    a = str(a)
    n = a
    cnt += 1

print(cnt)