import sys

n = int(sys.stdin.readline().rstrip())
input_list = map(int, sys.stdin.readline().rstrip().split(" "))

if (sum(input_list)/3).is_integer():
    print("yes")
else:
    print("no")