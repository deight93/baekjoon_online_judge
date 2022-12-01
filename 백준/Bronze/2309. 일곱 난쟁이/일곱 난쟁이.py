t_l = [int(input()) for i in range(9)]
tot = sum(t_l)
ck = False

for i in range(9):
    for j in range(i+1, 9):
        temp = tot - t_l[i] - t_l[j]
        if temp == 100:
            temp1 = t_l[i]
            temp2 = t_l[j]
            t_l.remove(temp1)
            t_l.remove(temp2)
            ck = True
            break
    if ck is True:
        break

for k in sorted(t_l):
    print(k)