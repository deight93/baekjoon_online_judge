
import sys

input_list = map(int, sys.stdin.readline().rstrip().split(" "))

t = 0
for i in input_list:
    t += i*5
print(t)
