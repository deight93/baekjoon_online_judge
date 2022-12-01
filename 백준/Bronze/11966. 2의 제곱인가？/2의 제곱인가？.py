
import sys

n = int(sys.stdin.readline().rstrip())

ck = 1
while True:
    if n == 1:
        break
    if n % 2 == 1:
        ck = 0
    n = n // 2

print(ck)