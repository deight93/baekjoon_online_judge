
import sys

n = int(sys.stdin.readline().rstrip())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]
input_list = sorted(input_list, key=lambda x: x[2], reverse=True)

temp = [0 for i in range(len(set([i[0] for i in input_list])))]
r_list = []
for i in input_list:
    temp[i[0]-1] += 1
    if temp[i[0]-1] <= 2:
        r_list += [(i[0], i[1])]

    if len(r_list) >= 3:
        break

for i in r_list:
    print(i[0], i[1])