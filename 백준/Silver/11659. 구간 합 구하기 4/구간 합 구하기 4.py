import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = tuple(map(int, sys.stdin.readline().rstrip().split(" ")))

sum_list = [0]
temp = 0
for i in input_list:
    temp += i
    sum_list += [temp]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    print(sum_list[j]-sum_list[i-1])