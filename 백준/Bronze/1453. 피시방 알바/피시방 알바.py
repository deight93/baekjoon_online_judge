import sys

n = int(sys.stdin.readline())

temp = []
temp2 = 0
for i in sys.stdin.readline().rstrip().split(" "):
    if i not in temp:
        temp += [i]
    else:
        temp2 += 1

print(temp2)