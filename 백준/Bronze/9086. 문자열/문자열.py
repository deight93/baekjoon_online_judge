import sys

t = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for i in range(t)]

for i in input_list:
    print("{}".format(i[0]+i[-1]))