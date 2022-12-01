import math
import sys

n = int(sys.stdin.readline())
if n <= 3:
    print(0)
else:
    print(int(math.factorial(n)/(math.factorial(4)*math.factorial(n-4))))