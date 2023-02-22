import sys

n = int(sys.stdin.readline().rstrip())
ck_n = 0
for _ in range(n):
    sn = int(sys.stdin.readline().rstrip())
    if ck_n == 0:
        ck_n = sn
        continue
    elif sn % ck_n == 0:
        print(sn)
        ck_n = 0

