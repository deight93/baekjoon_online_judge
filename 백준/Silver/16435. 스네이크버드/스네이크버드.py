import sys

n, l = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in input_list:
    if i <= l:
        l += 1

print(l)