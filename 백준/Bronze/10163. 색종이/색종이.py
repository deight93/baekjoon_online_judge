import sys

n = int(sys.stdin.readline().rstrip())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]


w = max(input_list, key=lambda x: x[0]+x[2])
h = max(input_list, key=lambda x: x[1]+x[3])
temp = [[0 for _ in range(w[0]+w[2]+1)] for _ in range(h[1]+h[3]+1)]

c = 0
for i in input_list:
    c += 1
    for x in range(i[0], i[0]+i[2]):
        for y in range(i[1], i[1]+i[3]):
            temp[y][x] = c

for k in range(c):
    total = 0
    for i in temp:
        a = [1 for j in i if j == k+1]
        total += sum(a)
    print(total)