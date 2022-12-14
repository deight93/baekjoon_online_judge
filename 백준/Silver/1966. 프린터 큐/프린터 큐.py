import sys
from collections import deque
import copy

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    w = map(int, sys.stdin.readline().rstrip().split(" "))
    dq = deque([(i, v)for i, v in enumerate(list(copy.deepcopy(w)))])
    s_w = deque(sorted(w, reverse=True))

    cnt = 0
    while True:
        if dq[0][1] == s_w[0]:
            cnt += 1
            if m == dq[0][0]:
                break
            dq.popleft()
            s_w.popleft()
        else:
            dq.rotate(-1)
    print(cnt)
