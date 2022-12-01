import sys
from itertools import combinations_with_replacement

input_list = list(map(int, sys.stdin.readline().split()))
for i in list(combinations_with_replacement([i for i in range(1, input_list[0]+1)], input_list[1])):
    for j in i:
        print(j, end=" ")
    print()