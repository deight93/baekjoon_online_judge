import sys
from itertools import permutations


n = int(sys.stdin.readline().rstrip())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

a = list(permutations(input_list, n))
temp = []
for i in a:
    total = 0
    for j in range(1, len(i)):
        total += abs(i[j-1]-i[j])
    temp += [total]

print(max(temp))