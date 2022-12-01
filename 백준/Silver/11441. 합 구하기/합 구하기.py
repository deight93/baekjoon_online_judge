
import sys

n_c = int(sys.stdin.readline().rstrip())
input_list = tuple(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline().rstrip())

prefix_sum = [0]
sum_v = 0
for i in input_list:
    sum_v += i
    prefix_sum += [sum_v]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    print(prefix_sum[j]-prefix_sum[i-1])