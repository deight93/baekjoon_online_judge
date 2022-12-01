import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n = map(int, sys.stdin.readline().rstrip().split(" "))

    input_dict = {}
    for i in range(m):
        for k, j in enumerate(sys.stdin.readline().rstrip().split(" ")):
            if k in input_dict.keys():
                input_dict[k] += [int(j)]
            else:
                input_dict[k] = [int(j)]

    total = 0
    for i in input_dict.values():
        for k, j in enumerate(i[:-1]):
            if j == 1:
                total += i[k:].count(0)
    print(total)