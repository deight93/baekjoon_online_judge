import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x = sys.stdin.readline().rstrip()
    len_x = len(x)
    x = int(x)

    for j in range(1, len_x):
        x = round(x+0.0000001, -1*j)
    print(int(x))

