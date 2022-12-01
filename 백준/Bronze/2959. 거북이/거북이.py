
import sys

input_list = sorted(map(int, sys.stdin.readline().rstrip().split(" ")))
print(min(input_list[:2])*min(input_list[2:]))