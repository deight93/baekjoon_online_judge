import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split(" "))

cnt = 0
while a != b:
    a -= a // 2
    b -= b // 2
    cnt += 1
print(cnt)
