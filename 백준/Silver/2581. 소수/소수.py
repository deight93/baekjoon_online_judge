a = int(input())
b = int(input())

pn_list = []
for i in range(a, b+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                pn_list += [j]
            else:
                break

if pn_list:
    print(sum(pn_list))
    print(min(pn_list))
else:
    print(-1)