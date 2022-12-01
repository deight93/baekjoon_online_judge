import sys

n = int(sys.stdin.readline())
input_list = [sum(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

[print(i) for i in input_list]