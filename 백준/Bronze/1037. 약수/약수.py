import sys

n = int(sys.stdin.readline())
input_list = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

print(input_list[-1]*input_list[0])