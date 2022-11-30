import math
import sys

n = int(sys.stdin.readline().rstrip())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

for i in input_list:
    a = math.factorial(i[1])//(math.factorial(i[0])*math.factorial(i[1]-i[0]))
    print(a)