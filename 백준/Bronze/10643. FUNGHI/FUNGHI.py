
import sys

m_list = [int(sys.stdin.readline().rstrip()) for _ in range(8)]

temp = []
for i in range(8):
    if i+4 > 8:
        temp += [sum(m_list[i:i+4] + m_list[:i+4-8])]
    else:
        temp += [sum(m_list[i:i + 4])]
print(max(temp))

