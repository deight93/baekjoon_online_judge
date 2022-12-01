import sys

input_list = sys.stdin.readline().rstrip().split(" ")

min_a = ""
min_b = ""
max_a = ""
max_b = ""

if "5" in input_list[0]:
    for i in input_list[0]:
        if i == "5":
            max_a += "6"
        else:
            max_a += i
else:
    max_a = input_list[0]

if "6" in input_list[0]:
    for i in input_list[0]:
        if i == "6":
            min_a += "5"
        else:
            min_a += i
else:
    min_a = input_list[0]

if "5" in input_list[1]:
    for i in input_list[1]:
        if i == "5":
            max_b += "6"
        else:
            max_b += i
else:
    max_b = input_list[1]

if "6" in input_list[1]:
    for i in input_list[1]:
        if i == "6":
            min_b += "5"
        else:
            min_b += i
else:
    min_b = input_list[1]

print(int(min_a)+int(min_b), int(max_a)+int(max_b))