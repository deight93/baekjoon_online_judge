import sys


def five_count(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt


def two_count(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt


n, m = map(int, sys.stdin.readline().split())


if m == 0:
    print(0)
else:
    print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))