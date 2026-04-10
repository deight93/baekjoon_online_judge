import sys

computer_nums = int(sys.stdin.readline())
couple_nums = int(sys.stdin.readline())

arr = [[] for _ in range(computer_nums + 1)]
for _ in range(couple_nums):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (computer_nums + 1)

def dfs(start, cnt):
    visited[start] = True
    for next_node in arr[start]:
        if not visited[next_node]:
            cnt += 1
            cnt = dfs(next_node, cnt)
    return cnt

r = 0
for i in range(1, computer_nums + 1):
    cnt = 0
    if not visited[i]:
        max_cnt = dfs(i, cnt)
        r = max(r, max_cnt)
print(r)