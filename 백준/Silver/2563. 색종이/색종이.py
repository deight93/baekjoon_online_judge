import sys

n = int(sys.stdin.readline().rstrip())
input_list = [[(int(j), int(j)+10) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

w = max(input_list, key=lambda x:x[0])[0][1]
h = max(input_list, key=lambda x:x[1])[1][1]
temp = [[0 for _ in range(w)] for _ in range(h)]

for i in input_list:
    for j in range(i[0][0]-1, i[0][1]-1):
        for k in range(i[1][0]-1, i[1][1]-1):
            temp[k][j] += 1

total = 0
for i in temp:
    a = [1 if j > 1 else j for j in i]
    total += sum(a)
print(total)