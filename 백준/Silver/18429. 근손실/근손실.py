import sys
from itertools import permutations

n, k = map(int, sys.stdin.readline().split())
arr = map(int, sys.stdin.readline().split())

cnt = 0
for i in permutations(arr, n):
    w = 500
    ck = True
    for j in i:
        temp = w-k+j
        if temp < 500:
             ck = False
             break
        w = temp

    if ck:
        cnt += 1
print(cnt)