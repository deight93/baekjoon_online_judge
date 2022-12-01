import sys

input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(2)]

a = 0
b = 0
for i in range(10):
    if input_list[0][i] > input_list[1][i]:
        a += 1
    elif input_list[0][i] < input_list[1][i]:
        b += 1
    else:
        pass

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("D")