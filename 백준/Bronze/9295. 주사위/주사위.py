import sys

n = int(sys.stdin.readline())
input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(n)]


for k, i in enumerate(input_list):
    print("Case {}: {}".format(k+1, sum(i)))
