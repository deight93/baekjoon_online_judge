import math

init = [int(i) for i in input().split(" ")]

p = init[0]
q = init[1]

temp = []
for i in range(1, p+1):
    if math.fmod(p, i) == 0:
        temp += [i]
    else:
        pass

if len(temp) < q:
    print(0)
else:
    print(temp[q - 1])