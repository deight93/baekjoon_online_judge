import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

temp = {}
for i in n_list:
    if i in temp.keys():
        temp[i] += 1
    else:
        temp[i] = 1

for j in m_list:
    if j in temp.keys():
        print(temp[j])
    else:
        print(0)