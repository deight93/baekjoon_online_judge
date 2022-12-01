import sys
from itertools import combinations

input_list = list(map(int, sys.stdin.readline().split()))
for i in list(combinations([i for i in range(1, input_list[0]+1)], input_list[1])):
    for j in i:
        print(j, end=" ")
    print()