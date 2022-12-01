
import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
temp = [0 for i in range(n)]
input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]

for i in input_list:
    for j in range(i[0]-1, i[1]):
        temp[j] = i[2]

print(" ".join([str(i) for i in temp]))