
import sys

n = int(sys.stdin.readline().rstrip())
input_list = [int(j) for j in sys.stdin.readline().rstrip().split(" ")]


total = 0
for i in input_list:
    for j in input_list:
        total += abs(i-j)
print(total)