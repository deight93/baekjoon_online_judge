import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    temp = {}
    d = 2
    while True:
        if n == 1:
            break

        if n % d == 0:
            if d in temp.keys():
                temp[d] += 1
            else:
                temp[d] = 1
            n = n//d
        else:
            d += 1

    for k, v in temp.items():
        print(k, v)