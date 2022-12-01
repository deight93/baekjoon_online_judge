import sys

n = int(sys.stdin.readline())
input_list = [float(sys.stdin.readline().rstrip())*0.8 for _ in range(n)]
[print("${:.2f}".format(i)) for i in input_list]