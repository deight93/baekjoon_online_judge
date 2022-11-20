import sys


def hanoi(n, a, b):
    if n == 1:
        print(a, b)
        return
    else:
        hanoi(n-1, a, 6-a-b)
        print(a, b)
        hanoi(n-1, 6-a-b, b)
        return


n = int(sys.stdin.readline().strip())
print(2**n-1)
a = 1
b = 3

hanoi(n, a, b)