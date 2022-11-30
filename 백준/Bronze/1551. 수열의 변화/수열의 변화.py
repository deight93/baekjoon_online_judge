
import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = list(map(int, sys.stdin.readline().rstrip().split(",")))

for i in range(k):
    temp = []
    for j in range(1, len(input_list)):
        temp += [input_list[j] - input_list[j-1]]
    input_list = temp
print(",".join([str(i) for i in input_list]))