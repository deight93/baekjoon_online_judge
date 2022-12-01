
import sys

t = int(sys.stdin.readline())

for t1 in range(t):
    input_list = [[int(j) for j in sys.stdin.readline().split(" ")] for i in range(9)]
    y = 0
    g = 0
    for i in input_list:
        y += i[0]
        g += i[1]

    if y > g:
        print("Yonsei")
    elif y < g:
        print("Korea")
    else:
        print("Draw")