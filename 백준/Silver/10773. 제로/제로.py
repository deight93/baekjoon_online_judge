
import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

temp = [0]
for i in input_list:
    if i != 0:
        temp += [i]
    else:
        temp.pop(-1)

print(sum(temp))