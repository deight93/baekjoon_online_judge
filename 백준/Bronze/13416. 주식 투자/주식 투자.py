import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    t = 0
    for _ in range(n):
        m_p = max(map(int, sys.stdin.readline().rstrip().split(" ")))
        if m_p >= 0:
            t += m_p
    print(t)

