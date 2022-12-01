import sys

a_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
b_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

t = 0
for i in range(3):
    temp = b_list[i] - a_list[i]
    if temp > 0:
        t += temp

print(t)