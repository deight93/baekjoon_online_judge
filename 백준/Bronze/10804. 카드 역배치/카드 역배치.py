
import sys

input_list = [[int(j)-1 for j in sys.stdin.readline().rstrip().split(" ")] for i in range(10)]
c_list = [i for i in range(1, 21)]

for i in input_list:
    temp = c_list[i[0]:i[1]+1]
    temp.reverse()
    c_list[i[0]:i[1] + 1] = temp

print(" ".join([str(i) for i in c_list]))