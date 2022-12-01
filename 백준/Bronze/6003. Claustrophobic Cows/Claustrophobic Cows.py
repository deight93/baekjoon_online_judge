import sys

n = int(sys.stdin.readline().rstrip())

ni = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

temp = [0, 1, (((ni[0][0]-ni[1][0])**2)+((ni[0][1]-ni[1][1])**2))**0.5]
for i in range(n):
    for j in range(1, n):
        if i != j:
            if temp[2] > (((ni[i][0]-ni[j][0])**2)+((ni[i][1]-ni[j][1])**2))**0.5:
                temp = [i, j, (((ni[i][0]-ni[j][0])**2)+((ni[i][1]-ni[j][1])**2))**0.5]

r = sorted([temp[0]+1, temp[1]+1])
print(r[0], r[1])

