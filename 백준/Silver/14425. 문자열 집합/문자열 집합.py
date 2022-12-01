import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
s = set([sys.stdin.readline().rstrip() for i in range(n)])
m_list = [sys.stdin.readline().rstrip() for i in range(m)]

cnt = 0
for i in m_list:
    if i in s:
       cnt += 1

print(cnt)
