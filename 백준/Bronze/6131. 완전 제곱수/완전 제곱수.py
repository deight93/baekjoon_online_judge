import sys

n = int(sys.stdin.readline().rstrip())

temp = 0
for b in range(1, 501):
    if (b+1 ** 2) - (b ** 2) > n:
        break
    for a in range(b, 501):
        if a**2 - b**2 == n:
            temp += 1

print(temp)