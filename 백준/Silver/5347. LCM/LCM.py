import math
import sys

n = int(sys.stdin.readline())
input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

for i in input_list:
    print(abs(i[0]*i[1]) // math.gcd(*i))