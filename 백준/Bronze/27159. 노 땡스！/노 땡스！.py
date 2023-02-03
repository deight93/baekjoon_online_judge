import sys

n = int(sys.stdin.readline().rstrip())
c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
m_c = c[0]
c_k = c[0]
r = m_c

for i in c[1:]:
    if i-c_k != 1:
        m_c = i
        r += m_c
    c_k = i

print(r)