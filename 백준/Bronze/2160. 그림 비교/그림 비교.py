import sys

n = int(sys.stdin.readline().rstrip())

p_list = [[sys.stdin.readline().rstrip() for i in range(5)] for _ in range(n)]

temp = []
for i in range(n):
    a = p_list[i]
    for j in range(i+1, n):
        b = p_list[j]
        diff_cnt = len([(i,j) for i, row in enumerate(a) for j, x in enumerate(row) if b[i][j] != x])
        temp += [[(str(i+1), str(j+1)), diff_cnt]]

print(" ".join(min(temp, key=lambda x: x[1])[0]))
