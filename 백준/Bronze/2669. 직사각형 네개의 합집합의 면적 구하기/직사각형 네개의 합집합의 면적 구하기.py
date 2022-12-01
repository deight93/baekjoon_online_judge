
import sys

input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(4)]

w = max(input_list, key=lambda x:x[2])[2]
h = max(input_list, key=lambda x:x[3])[3]
temp = [[0 for _ in range(w)] for _ in range(h)]

for i in input_list:
    for x in range(i[0]-1, i[2]-1):
        for y in range(i[1]-1, i[3]-1):
            temp[y][x] += 1

total = 0
for i in temp:
    a = [1 if j > 1 else j for j in i]
    total += sum(a)
print(total)
