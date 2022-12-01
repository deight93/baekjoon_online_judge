import sys

from itertools import combinations

input_list = [int(sys.stdin.readline().rstrip()) for i in range(9)]

for i in list(combinations(input_list, 2)):
    a = input_list.copy()
    a.remove(i[0])
    a.remove(i[1])

    if sum(a) == 100:
        for j in a:
            print(j)
        break
