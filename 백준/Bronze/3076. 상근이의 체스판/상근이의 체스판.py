import sys

r, c = map(int, sys.stdin.readline().rstrip().split(" "))
a, b = map(int, sys.stdin.readline().rstrip().split(" "))

for y in range(r):
    temp = ""
    for x in range(c):
        if y % 2 == 0 and x % 2 == 0:
            s = "X"*b
        elif y % 2 == 0 and x % 2 == 1:
            s = "." * b
        elif y % 2 == 1 and x % 2 == 0:
            s = "." * b
        elif y % 2 == 1 and x % 2 == 1:
            s = "X" * b
        temp += s
    for i in range(a):
        print(temp)