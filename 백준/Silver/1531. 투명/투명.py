
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

temp = [[0 for _ in range(101)] for _ in range(101)]

for i in input_list:
    for x in range(i[0], i[2]+1):
        for y in range(i[1], i[3]+1):
            temp[y][x] += 1

total = 0
for i in temp:
    a = [1 for j in i if j > m]
    total += sum(a)
print(total)