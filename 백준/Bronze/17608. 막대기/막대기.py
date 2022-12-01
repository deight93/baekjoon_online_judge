import sys

n = int(sys.stdin.readline().rstrip())
num = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

max_h = num[-1]
ck = 1
for i in num[::-1]:
    if i > max_h:
        ck += 1
        max_h = i
print(ck)

