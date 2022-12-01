import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in input_list:
    print(i[::-1])