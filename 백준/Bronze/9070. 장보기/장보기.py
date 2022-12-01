import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    temp = []
    for i in range(n):
        w, c = map(int, sys.stdin.readline().strip().split(" "))
        temp += [(w, c, c/w)]
    print(min(sorted(temp, key=lambda x: x[1]), key=lambda x: x[2])[1])

