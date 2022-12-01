import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().lower() for _ in range(n)]

[print(i) for i in input_list]