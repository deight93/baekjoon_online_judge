
import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
v = int(sys.stdin.readline())

print(input_list.count(v))