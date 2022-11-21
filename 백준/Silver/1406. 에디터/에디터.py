import sys
import collections

c = list(sys.stdin.readline().rstrip())
dq = collections.deque(c)
dq2 = collections.deque()
n = int(sys.stdin.readline())
cmd_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

for i in cmd_list:
    if i[0] == "L" and dq:
        dq2.appendleft(dq.pop())
    elif i[0] == "D" and dq2:
        dq.append(dq2.popleft())
    elif i[0] == "B" and dq:
        dq.pop()
    elif i[0] == "P":
        dq.append(i[1])

print("".join(dq+dq2))