import sys

n = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    stack = list()

    for i in w:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if not stack:
        cnt += 1
print(cnt)

