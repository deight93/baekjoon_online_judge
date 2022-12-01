import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    input_list = sys.stdin.readline().rstrip().split(" ")
    a_c = input_list[0].count(input_list[1])

    print(len(input_list[0])-(a_c*len(input_list[1]))+a_c)