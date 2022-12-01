import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
input_s_list = [[int(j) for j in sys.stdin.readline().split(" ")] for i in range(n)]

k = [i for i in range(n)]

comb_list = list(combinations(k, int(n/2)))

temp = []
for i in comb_list:
    temp2 = 0
    for j in list(combinations(i, int(2))):
        temp2 += input_s_list[j[0]][j[1]]+input_s_list[j[1]][j[0]]
    temp += [temp2]

temp3 = []
for j in range(int(len(temp)/2)):
    temp3 += [abs(temp[j]-temp[-(j+1)])]

print(min(temp3))