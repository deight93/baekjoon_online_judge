import sys
import math

n = sys.stdin.readline().rstrip()

temp = {}
for i in set(n):
    if i == '9' or i == '6':
        if '6' in temp.keys():
            temp['6'] += (n.count(i)/2)
        else:
            temp['6'] = n.count(i)/2
    else:
        temp[i] = n.count(i)

print(int(math.ceil(max(temp.items(), key=lambda x: x[1])[1])))