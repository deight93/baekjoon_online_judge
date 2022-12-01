import sys

c = int(input())
for i in range(c):
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    print(input_list[0]+input_list[1])