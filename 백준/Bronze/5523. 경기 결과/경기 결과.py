import sys

n = int(sys.stdin.readline())
input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(n)]

a = 0
b = 0
for i in input_list:
    if i[0] > i[1]:
        a += 1
    elif i[0] < i[1]:
        b += 1
    else:
        pass

print(a, b)