import sys

n, w, h = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

d = (w**2+h**2)**0.5

for i in input_list:
    if i <= w or i <= h or i <= d:
        print("DA")
    else:
        print("NE")