import sys

n, m, = map(int, sys.stdin.readline().strip().split(" "))

s_list = [sys.stdin.readline().strip() for _ in range(n)]
c_list = [sys.stdin.readline().strip() for _ in range(m)]

s_list.sort()
c_list.sort()

cnt = 0
idx = 0
for c in c_list:
    for s in range(idx, len(s_list)):
        if s_list[s].startswith(c):
            cnt += 1
            idx = s
            break

print(cnt)


