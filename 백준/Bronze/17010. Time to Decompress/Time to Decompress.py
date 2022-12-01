
import sys

input_list = [sys.stdin.readline().rstrip().split(" ") for i in range(int(sys.stdin.readline().rstrip()))]

for i in input_list:
    print(i[1]*int(i[0]))