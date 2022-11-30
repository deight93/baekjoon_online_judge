import sys

n = int(sys.stdin.readline())
word_list = set([sys.stdin.readline().strip() for i in range(n)])

temp = {}
for i in word_list:
    if len(i) in temp.keys():
        temp[len(i)] += [i]
    else:
        temp[len(i)] = [i]

for k,v in temp.items():
    temp[k] = sorted(v)

word_list2 = sorted(temp.items(), key=lambda x: (x[0]))

for i in word_list2:
    for j in i[1]:
        print(j)