import sys

n = int(sys.stdin.readline())

a = 100
b = 100

for i in range(n):
    input_list = [int(i) for i in sys.stdin.readline().split()]
    if input_list[0] > input_list[1]:
        b -= input_list[0]
    elif input_list[0] < input_list[1]:
        a -= input_list[1]
    else:
        pass

print(a)
print(b)