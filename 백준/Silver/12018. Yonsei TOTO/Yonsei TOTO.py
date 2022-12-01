
import sys


n, m = map(int, sys.stdin.readline().rstrip().split(" "))
temp = []
for _ in range(n):
    pi, li = map(int, sys.stdin.readline().rstrip().split(" "))
    m_list = sorted(map(int, sys.stdin.readline().rstrip().split(" ")), reverse=True)

    if pi < li:
        temp.append(1)
    else:
        if m_list.count(m_list[li-1]) > 1:
            temp.append(m_list[li-1])
        else:
            temp.append(m_list[li-1])

cnt = 0
t = 0
for i in sorted(temp):
    t += i
    if t <= m:
        cnt += 1

print(cnt)
