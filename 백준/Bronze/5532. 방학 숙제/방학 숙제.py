import sys
import math

input_list = [int(sys.stdin.readline().rstrip()) for _ in range(5)]
print(input_list[0]-max(math.ceil(input_list[1]/input_list[3]), math.ceil(input_list[2]/input_list[4])))