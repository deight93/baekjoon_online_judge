import sys

r, c = map(int, sys.stdin.readline().rstrip().split(" "))
i_l = [sys.stdin.readline().rstrip() for _ in range(r)]
a, b = map(int, sys.stdin.readline().rstrip().split(" "))

for i in range(r):
    i_l[i] = i_l[i]+i_l[i][::-1]

i_l = i_l + i_l[::-1]
i_l = list(i_l)
i_l[a - 1] = list(i_l[a - 1])
if i_l[a-1][b-1] == ".":
    i_l[a-1][b-1] = "#"
else:
    i_l[a-1][b-1] = "."
i_l[a-1] = "".join(i_l[a-1])

for i in i_l:
    print(i)
