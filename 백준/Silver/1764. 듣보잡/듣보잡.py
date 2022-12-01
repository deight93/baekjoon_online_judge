import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
n_list = [sys.stdin.readline().rstrip() for _ in range(n)]
m_list = [sys.stdin.readline().rstrip() for _ in range(m)]

temp = sorted(list(set(n_list) & set(m_list)))
print(len(temp))
[print(i) for i in temp]