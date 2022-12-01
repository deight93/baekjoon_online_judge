import sys

t = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(t)]

for i in input_list:
    a = [int(str(j).count("0")) for j in range(i[0], i[1]+1) if str(j).find("0") != -1]
    print(sum(a))