import collections


def solution(n, wires):
    answer = n+1

    for i, _ in enumerate(wires):
        graph = [[] for _ in range(n+1)]
        for j, (a, b) in enumerate(wires):
            if i == j: continue
            graph[a].append(b)
            graph[b].append(a)
        cnt = bfs(graph, i+1)
        answer = min(answer, abs(n - 2 * cnt))

    return answer

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = collections.deque([start])
    visited[start] = True
    count = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count