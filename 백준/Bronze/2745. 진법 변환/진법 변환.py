
import sys

input_list = sys.stdin.readline().rstrip().split(" ")
N = input_list[0]
B = int(input_list[1])

temp = {}
for i in range(65, 91):
    temp[chr(i)] = i-55

s = 0
for i in range(len(N)):
    p = len(N)-i-1
    if N[i].isalpha():
        s += temp[N[i]] * (B**p)
    else:
        s += int(N[i]) * (B ** p)

print(s)