import sys

n = int(sys.stdin.readline().rstrip())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

[print("NO BRAINS") if i[0] < i[1] else print("MMM BRAINS") for i in input_list]