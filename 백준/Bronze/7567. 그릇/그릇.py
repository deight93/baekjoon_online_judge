import sys

input_list = [i for i in sys.stdin.readline().rstrip()]

temp = ""
h = 0
for i in input_list:
    if temp == "":
        h += 10
        temp = i
    else:
        if temp == i:
            h += 5
            temp = i
        else:
            h += 10
            temp = i

print(h)