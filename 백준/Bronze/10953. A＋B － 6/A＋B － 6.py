import sys

t = int(sys.stdin.readline())
input_list = [sum([int(j) for j in sys.stdin.readline().rstrip().split(",")]) for i in range(t)]
[print(i) for i in input_list]