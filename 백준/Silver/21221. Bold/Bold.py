num: 21221
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
s = []
temp = []
for i in range(n):
    w = list(sys.stdin.readline().rstrip())
    s.append(w)
    for j in range(m):
        if w[j] == "#":
            temp.append([i, j])


for i in temp:
    s[i[0]][i[1]+1] = "#"
    s[i[0]+1][i[1] + 1] = "#"
    s[i[0]+1][i[1]] = "#"

for i in s:
    print("".join(i))