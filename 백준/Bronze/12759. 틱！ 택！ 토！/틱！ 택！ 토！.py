
import sys

p = int(sys.stdin.readline().rstrip())
if p == 1:
    p2 = 2
else:
    p2 = 1

temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for n in range(1, 10):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    if n % 2 == 1:
        a = 5
    else:
        a = 20

    temp[x-1][y-1] = a

    ck = 0
    for i in range(3):
        if sum(temp[i]) == 15:
            print(p)
            ck = 1
            break
        elif sum(temp[i]) == 60:
            print(p2)
            ck = 1
            break

        if sum([j[i] for j in temp]) == 15:
            print(p)
            ck = 1
            break
        elif sum([j[i] for j in temp]) == 60:
            print(p2)
            ck = 1
            break
    if ck == 1:
        break

    if sum([temp[j][j] for j in range(3)]) == 15:
        print(p)
        ck = 1
        break
    elif sum([temp[j][j] for j in range(3)]) == 60:
        print(p2)
        ck = 1
        break

    if sum([temp[2-j][j] for j in range(3)]) == 15:
        print(p)
        ck = 1
        break
    elif sum([temp[2-j][j] for j in range(3)]) == 60:
        print(p2)
        ck = 1
        break

if ck == 0:
    print(0)