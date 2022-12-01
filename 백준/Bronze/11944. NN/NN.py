import sys

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

temp = ""
for i in range(input_list[0]):
    temp += str(input_list[0])

print(temp[:input_list[1]])