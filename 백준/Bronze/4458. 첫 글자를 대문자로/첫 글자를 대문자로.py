
import sys

n = int(sys.stdin.readline())

input_list = [sys.stdin.readline().rstrip() for i in range(n)]

for i in input_list:
    i[0].upper()
    print(i[0].upper()+i[1:])