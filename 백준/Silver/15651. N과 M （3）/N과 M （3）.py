import sys
from itertools import product

input_list = list(map(int, sys.stdin.readline().split()))
for i in list(product([i for i in range(1, input_list[0]+1)], repeat=input_list[1])):
    for j in i:
        print(j, end=" ")
    print()