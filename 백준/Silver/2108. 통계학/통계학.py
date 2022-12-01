import sys
from collections import Counter

c = int(sys.stdin.readline())

n_list = [int(sys.stdin.readline()) for i in range(c)]

print(round(sum(n_list)/len(n_list)))
print(sorted(n_list)[len(n_list)//2])
a = Counter(n_list)
b = max(a.values())
c = sorted([k for k, v in a.items() if v == b])
if len(c) == 1:
    print(c[0])
else:
    print(c[1])
print(max(n_list)-min(n_list))