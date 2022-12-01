import sys

input_list = [int(sys.stdin.readline().rstrip()) for _ in range(10)]

a = input_list[0]
for i in input_list[1:]:
    a -= i

print(a)