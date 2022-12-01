temp = []
for i in range(3):
    input_list = [int(i) for i in input().split(" ")]
    temp += [tuple(input_list)]

temp2 = []
for i in temp:
    for j in temp:
        temp2 += [(i[0], j[1])]
set_temp = set(temp2)

for i in temp:
    set_temp.remove(i)

print(list(set_temp)[0][0], list(set_temp)[0][1])