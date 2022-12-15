import sys
from collections import deque


n, w, l = map(int, sys.stdin.readline().rstrip().split(" "))
an = deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
w = deque([0 for i in range(w)])

cnt = 0
while True:
    if not an and sum(w) == 0:
        break
    else:
        w.popleft()
        if not an or sum(w) + an[0] > l:
            w.append(0)
        else:
            w.append(an[0])
            an.popleft()
        cnt += 1

print(cnt)

