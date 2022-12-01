import collections
import sys

dq = collections.deque()
n = int(sys.stdin.readline())
cmd_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

for i in cmd_list:
    if i[0] == "push":
        dq.appendleft(int(i[1]))
    elif i[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif i[0] == "size":
        print(len(dq))
    elif i[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == "top":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])