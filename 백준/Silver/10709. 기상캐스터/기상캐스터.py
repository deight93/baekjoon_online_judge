
import sys

h, w = map(int, sys.stdin.readline().rstrip().split(" "))
a = [sys.stdin.readline().rstrip() for _ in range(h)]
b = [[0 if j == "c" else -1 for j in i] for i in a]

for i in b:
    for j in range(1, w):
        if i[j-1] == 0 and i[j] != 0:
            i[j] = 1
        elif i[j-1] > 0 and i[j] != 0:
            i[j] = i[j-1]+1

for i in b:
    print(" ".join([str(j) for j in i]))
