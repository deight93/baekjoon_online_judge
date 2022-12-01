import math
import sys

n = int(sys.stdin.readline().rstrip())
temp = str(math.factorial(n))[::-1]

cnt = 0
for i in temp:
    if i != "0":
        break
    else:
        cnt += 1
print(cnt)