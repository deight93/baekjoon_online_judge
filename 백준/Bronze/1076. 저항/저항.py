import sys
temp_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
temp_dict = {}
a = 0
b = 1
for _ in temp_list:
    temp_dict[_] = [str(a), b]
    a += 1
    b *= 10

input_list = [sys.stdin.readline().rstrip() for _ in range(3)]

total = ""
for k, i in enumerate(input_list):
    if k == 0:
        total += temp_dict[i][0]
    elif k == 1:
        total += temp_dict[i][0]
        total = int(total)
    else:
        total *= temp_dict[i][1]
print(total)