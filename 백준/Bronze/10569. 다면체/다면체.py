import sys

n = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

for i in input_list:
    print(2-i[0]+i[1])