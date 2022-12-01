import math
import sys

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
a = int(math.factorial(input_list[0])/(math.factorial(input_list[1])*math.factorial(input_list[0]-input_list[1])))
print(a)
