import sys

n_a, n_l = map(int, sys.stdin.readline().rstrip().split(" "))
m_a, m_l = map(int, sys.stdin.readline().rstrip().split(" "))

while True:
    n_l -= m_a
    m_l -= n_a

    if n_l <= 0 and m_l <= 0:
        print("DRAW")
        break
    elif n_l <= 0:
        print("PLAYER B")
        break
    elif m_l <= 0:
        print("PLAYER A")
        break