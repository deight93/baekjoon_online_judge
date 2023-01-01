import sys

n = int(sys.stdin.readline().rstrip())

ck = False
for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    r_n = sys.stdin.readline().rstrip()
    m_n = [sys.stdin.readline().rstrip() for i in range(k)]
    if "pea soup" in m_n and "pancakes" in m_n:
        ck = r_n
        break

if ck is False:
    print("Anywhere is fine I guess")
else:
    print(ck)

