import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

init = 0
total = 0
for i in input_list:
    if i == 1:
        init += 1
    else:
        init = 0
    total += init

print(total)