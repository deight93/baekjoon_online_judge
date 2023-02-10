import sys

s = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()
m = len(boom)
stack = list()

for i in s:
    stack.append(i)
    if i == boom[-1] and "".join(stack[-m:]) == boom:
        del stack[-m:]

if stack:
    print("".join(stack))
else:
    print("FRULA")