import sys

n = int(sys.stdin.readline())
temp = [int(sys.stdin.readline()) for _ in range(n)]

arr = [[] for _ in range(n+1)]
for i in range(1, n+1):
    arr[i].append(temp[i-1])


r = []
def dfs(start, node):
    visited[node] = True

    for next_node in arr[node]:
        if not visited[next_node]:
            dfs(start, next_node)
        if start == next_node:
            r.append(start)

for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)

print(len(r))
for i in sorted(r):
    print(i)