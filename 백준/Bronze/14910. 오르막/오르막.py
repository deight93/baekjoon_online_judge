import sys

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

a2 = "Good"
for i in range(1, len(input_list)):
    if input_list[i-1] > input_list[i]:
        a2 = "Bad"
        break
print(a2)