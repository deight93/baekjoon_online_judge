import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    print(sum(input_list))