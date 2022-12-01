import sys

w = sys.stdin.readline().rstrip()
temp = [1, 0, 0]

for i in w:
    a = temp[0]
    b = temp[1]
    c = temp[2]
    if i == "A":
        temp[0] = b
        temp[1] = a
    elif i == "B":
        temp[1] = c
        temp[2] = b
    elif i == "C":
        temp[0] = c
        temp[2] = a

print(temp.index(1)+1)