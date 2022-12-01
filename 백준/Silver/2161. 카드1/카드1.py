import sys
from collections import deque

n = int(sys.stdin.readline())
n_list = [i+1 for i in range(n)]
deq = deque(n_list)
temp = []

for i in range(n):
    temp += [str(list(deq)[0])]
    deq.popleft()
    deq.rotate(-1)

print(" ".join(temp))