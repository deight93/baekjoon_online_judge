
import sys
import re
import itertools

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]
temp = sorted(["".join(i) for i in set(list(itertools.combinations('HTHTHT', 3)))], reverse=True)

for i in input_list:
    temp2 = []
    for j in temp:
        temp2 += [str(len(re.findall('(?={})'.format(j), i)))]
    print(" ".join(temp2))