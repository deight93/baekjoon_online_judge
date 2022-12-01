import sys

n = int(sys.stdin.readline().rstrip())
input_list = sorted(set(map(int, sys.stdin.readline().rstrip().split(" "))))
[print(i, end=" ") for i in input_list]
