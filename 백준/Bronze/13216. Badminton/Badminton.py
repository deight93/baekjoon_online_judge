
import sys

s = sys.stdin.readline().rstrip()

w = [[0, 0, "A"], [0, 0, "B"]]
for i in s:
    if i == "A":
        w[0][0] += 1
    else:
        w[1][0] += 1

    if w[0][0] == 21:
        print("{}-{}".format(w[0][0], w[1][0]))
        w[0][0], w[1][0] = 0, 0
        w[0][1] += 1

    if w[1][0] == 21:
        print("{}-{}".format(w[0][0], w[1][0]))
        w[0][0], w[1][0] = 0, 0
        w[1][1] += 1

print(max(w, key=lambda x:x[1])[2])


