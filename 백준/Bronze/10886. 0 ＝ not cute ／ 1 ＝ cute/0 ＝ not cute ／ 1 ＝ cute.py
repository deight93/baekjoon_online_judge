
import sys

n = int(sys.stdin.readline())

temp_list = []
for i in range(n):
    temp_list += [int(sys.stdin.readline())]

if temp_list.count(1) > temp_list.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")