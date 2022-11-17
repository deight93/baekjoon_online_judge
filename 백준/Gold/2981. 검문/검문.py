import math
import sys
from functools import reduce

n = int(sys.stdin.readline().rstrip())

input_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]

temp = []
for i in range(1, n):
    temp += [abs(input_list[i]-input_list[i-1])]

num = reduce(lambda x, y: math.gcd(x, y), temp)

a2 = []
for x in range(2, num+1):
    if num % x == 0:
        a2.append(x)

[print(i, end=" ") for i in a2]