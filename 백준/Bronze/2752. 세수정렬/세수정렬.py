
import sys

input_list = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
[print(_, end=" ") for _ in input_list]