import math
import sys


dp = [math.factorial(i) for i in range(1001)]

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
a = input_list[0]
b = input_list[1]

v = (dp[a]//(dp[b]*dp[a-b])) % 10007
print(v)
