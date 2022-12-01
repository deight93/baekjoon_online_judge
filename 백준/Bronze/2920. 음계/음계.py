import sys

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

temp = []
for i in range(1, len(input_list)):
    temp += [input_list[i]-input_list[i-1]]

temp_set = list(set(temp))
if len(temp_set) == 1:
    if temp[0] == 1:
        print("ascending")
    else:
        print("descending")
else:
    print("mixed")
