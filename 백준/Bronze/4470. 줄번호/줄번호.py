import sys

n = int(sys.stdin.readline())

input_list = [sys.stdin.readline().rstrip() for i in range(n)]

for k, i in enumerate(input_list):
    print("{}. {}".format(k+1, i))