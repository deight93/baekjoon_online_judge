import sys
import math

n = int(sys.stdin.readline())

for _ in range(n):
    input_list = sys.stdin.readline().rstrip().split(" ")
    a, b = sorted(map(int, input_list), reverse=True)
    print((math.ceil(a/b))**2)
