import sys


def p_pow(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        temp = p_pow(a, b//2, c)
        return temp*temp%c
    else:
        temp = p_pow(a, (b-1)//2, c)
        return temp*temp*a%c


a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
print(p_pow(a, b, c))
