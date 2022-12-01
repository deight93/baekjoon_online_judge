import sys

n = int(sys.stdin.readline().rstrip())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]

if input_list == sorted(input_list):
    print("INCREASING")
elif input_list == sorted(input_list, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
