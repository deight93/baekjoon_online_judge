from collections import deque

def solution(n, edge):

    graph = {}
    for e in edge:
        graph.setdefault(e[0], set()).add(e[1])
        graph.setdefault(e[1], set()).add(e[0])

    for k, v in graph.items():
        graph[k] = {"cnt": 0, "edges": v}



    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]["edges"]:
            if not visited[i]:
                visited[i] = True
                graph[i]["cnt"] = graph[v]["cnt"] + 1
                queue.append(i)

    return [i["cnt"] for i in graph.values()].count(max(graph.values(), key=lambda x: x["cnt"])["cnt"])
