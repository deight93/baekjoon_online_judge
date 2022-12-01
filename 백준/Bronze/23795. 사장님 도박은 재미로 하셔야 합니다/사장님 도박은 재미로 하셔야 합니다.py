
import sys

total = 0
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        print(total)
        break
    else:
        total += n