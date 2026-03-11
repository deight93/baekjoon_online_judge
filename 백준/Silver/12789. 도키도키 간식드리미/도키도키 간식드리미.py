from collections import deque

n = int(input())
students = deque(map(int, input().split()))

r = []
expected = 1

while students:
    if r:
        if r[-1] == expected:
            r.pop()
            expected += 1
            continue

    s = students.popleft()
    if s == expected:
        expected += 1
    else:
        r.append(s)

for i in range(len(r)):
    if r[-1] == expected:
        r.pop()
        expected += 1

if r:
    print("Sad")
else:
    print("Nice")