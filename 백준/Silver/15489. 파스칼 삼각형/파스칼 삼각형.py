import sys

r, c, w = map(int, sys.stdin.readline().rstrip().split(" "))
p_t = [[1] for _ in range(30)]

for i in range(1, 30):
    for j in range(i+1):
        if j == 0:
            pass
        elif j == i:
            p_t[i].append(1)
        else:
            p_t[i].append(p_t[i-1][j-1]+p_t[i-1][j])

t = 0
y = 0
for x in range(r-1, r+w-1):
    y += 1
    t += sum(p_t[x][c-1:c-1+y])
print(t)


