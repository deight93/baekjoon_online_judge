a = [int(input()) for i in range(3)]

temp = 1
for i in a:
    temp = temp*i

temp2 = [{str(i): 0} for i in range(0,10)]

for i in str(temp):
    for j in temp2:
        if list(j.keys())[0] == i:
            j[i] += 1

for k in temp2:
    print(list(k.values())[0])