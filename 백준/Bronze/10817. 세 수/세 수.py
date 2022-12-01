
import sys

input_list = [int(i) for i in sys.stdin.readline().split(" ")]
input_list.sort()

print(input_list[1])
