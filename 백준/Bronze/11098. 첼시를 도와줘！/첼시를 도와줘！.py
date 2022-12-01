import sys

t = int(sys.stdin.readline())
temp = []
for i in range(t):
    n = int(sys.stdin.readline())
    input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

    a = max(input_list, key=lambda x: int(x[0]))
    temp += [a[1]]

[print(i) for i in temp]