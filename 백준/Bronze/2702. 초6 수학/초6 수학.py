import math
import sys

n = int(sys.stdin.readline())
input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(n)]

for i in input_list:
    print(abs(i[0]*i[1]) // math.gcd(*i), math.gcd(*i))