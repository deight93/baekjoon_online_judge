import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split(" "))
    input_list = list(map(int, sys.stdin.readline().split(" ")))

    total = 0
    for i in input_list:
        total += i//k
    print(total)