import sys

while True:
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    if n == 0 and m == 0:
        break
    else:
        temp = [0 for _ in range(n)]
        for _ in range(m):
            for i, v in enumerate(list(map(int, sys.stdin.readline().rstrip().split(" ")))):
                temp[i] += v
        print(max(temp))
