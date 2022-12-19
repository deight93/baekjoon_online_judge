import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    y, m = map(int, sys.stdin.readline().rstrip().split(" "))
    if m == 1:
        m_1 = 12
    else:
        m_1 = m-1

    if m_1 in [1, 3, 5, 7, 8, 10, 12]:
        if m_1 == 12:
            print(y - 1, 12, 31)
        else:
            print(y, m-1, 31)
    elif m_1 == 2:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            print(y, m - 1, 29)
        else:
            print(y, m - 1, 28)
    elif m_1 in [4, 6, 9, 11]:
        print(y, m - 1, 30)


