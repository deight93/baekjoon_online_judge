import sys

n = int(sys.stdin.readline())

def factorial(a, cnt, n):
    cnt += 1
    b = a*(cnt)
    if n <= 1:
        print(a)
    elif cnt == n:
        print(b)
        return b
    else:
        factorial(b, cnt, n)

factorial(1, 1, n)