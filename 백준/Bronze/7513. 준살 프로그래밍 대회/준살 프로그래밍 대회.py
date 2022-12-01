import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    m = int(sys.stdin.readline().rstrip())
    m_list = [sys.stdin.readline().strip() for _ in range(m)]
    n = int(sys.stdin.readline().rstrip())
    n_list = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]

    print("Scenario #{}:".format(i+1))
    for j in n_list:
        print(''.join([m_list[k] for k in [i for i in j[1:]]]))
    print()

