import sys

p_list = [350.34, 230.90, 190.55, 125.30, 180.90]

n = int(sys.stdin.readline())
input_list = [sum([x*y for x, y in zip(list(map(int, sys.stdin.readline().rstrip().split(" "))),p_list)]) for _ in range(n)]
[print("${:.2f}".format(i)) for i in input_list]