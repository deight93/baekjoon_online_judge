import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
print(input_list[k-1])