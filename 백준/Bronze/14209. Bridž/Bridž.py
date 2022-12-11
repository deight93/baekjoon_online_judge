import sys

n = int(sys.stdin.readline().rstrip())
temp = {"A": 4, "K": 3, "Q": 2, "J": 1, "X": 0}

r = 0
for _ in range(n):
    ki = sys.stdin.readline().rstrip()

    for i in ki:
        r += temp[i]
print(r)
