import sys

n = sys.stdin.readline().rstrip()
temp = [1, 0, 0]

for i in n:
    if i == "A":
        temp[0], temp[1] = temp[1], temp[0]
    elif i == "B":
        temp[1], temp[2] = temp[2], temp[1]
    else:
        temp[0], temp[2] = temp[2], temp[0]
print(temp.index(1)+1)