import sys
import itertools

li = list(map(int, sys.stdin.readline().rstrip().split(" ")))
cnt = 0
for i in list(itertools.combinations(li, 3)):
    if i[0] + i[1] > i[2] and i[0] + i[2] > i[1] and i[1] + i[2] > i[0]:
        cnt += 1
print(cnt)


