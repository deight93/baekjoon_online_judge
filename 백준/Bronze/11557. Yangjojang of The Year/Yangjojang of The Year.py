import sys

t = int(sys.stdin.readline())

for t1 in range(t):
    n = int(sys.stdin.readline())
    input_list = [[j for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]
    print(max(input_list, key=lambda x: int(x[1]))[0])