import sys

n, b, h, w = map(int, sys.stdin.readline().rstrip().split(" "))

mp = []
for _ in range(h):
    p = int(sys.stdin.readline().rstrip())
    a = map(int, sys.stdin.readline().rstrip().split(" "))

    if n * p <= b:
        for i in a:
            if i >= n:
                mp.append(n * p)
                break
if mp:
    print(min(mp))
else:
    print("stay home")

