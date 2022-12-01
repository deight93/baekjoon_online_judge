import sys
import re

input_list = [sys.stdin.readline().rstrip() for _ in range(3)]

for i in input_list:
    temp = 1
    for j in range(0, 10):
        temp2 = re.findall('{}+'.format(str(j)), i)
        for k in temp2:
            if len(k) > temp:
                temp = len(k)
    print(temp)