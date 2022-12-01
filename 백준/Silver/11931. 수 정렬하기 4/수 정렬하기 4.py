import sys

n = int(sys.stdin.readline().rstrip())
input_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)
[print(i) for i in input_list]