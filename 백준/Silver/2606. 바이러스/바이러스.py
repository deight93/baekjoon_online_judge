import sys

n = int(sys.stdin.readline())
e = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(e)]

temp = []
for i in input_list:
    if 1 in i:
        temp += i
        input_list.remove(i)

temp = list(set(temp))
while True:
    k = len(temp)
    for i in input_list:
        for j in i:
            if j in temp:
                temp += i
    temp = list(set(temp))
    if len(temp) == k:
        break

temp.remove(1)
print(len(temp))