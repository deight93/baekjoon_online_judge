
import sys

n = int(sys.stdin.readline().rstrip())

temp = {"A": 1, "B": 2, "D": 1, "O": 1, "P": 1, "Q": 1, "R": 1}

for _ in range(n):
    c = sys.stdin.readline().rstrip()
    t = 0
    for i in c:
        if i in temp.keys():
            t += temp[i]
    print(t)

