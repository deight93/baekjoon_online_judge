
import sys

temp = [(30, 40), (35, 30), (40, 20)]

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    if [a, b] == [0, 0]:
        break
    else:
        print(min([i[0]*a+i[1]*b for i in temp]))
