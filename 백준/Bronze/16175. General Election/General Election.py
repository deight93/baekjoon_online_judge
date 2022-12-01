import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    s = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]
    s_s = [sum(i) for i in list(zip(*s))]
    print(s_s.index(max(s_s))+1)