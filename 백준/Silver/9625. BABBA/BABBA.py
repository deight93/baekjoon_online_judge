import sys

n = int(sys.stdin.readline())
temp = [(1, 0), (0, 1), (1, 1)]

for i in range(2, n):
    temp.append((temp[i][0]+temp[i-1][0], temp[i][1]+temp[i-1][1]))

if n <= 2:
    print(temp[n][0], temp[n][1])
else:
    print(temp[-1][0], temp[-1][1])