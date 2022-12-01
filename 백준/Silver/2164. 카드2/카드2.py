
import sys
from collections import deque

n = int(sys.stdin.readline())
n_list = [i+1 for i in range(n)]
deq = deque(n_list)


for i in range(n):
    if i+1 == n:
        print(list(deq)[0])
    deq.popleft()
    deq.rotate(-1)