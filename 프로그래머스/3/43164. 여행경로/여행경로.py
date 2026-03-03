def solution(tickets):
    graph = {}
    for a, b in tickets:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, [])

    for k in graph.keys():
        graph[k].sort(reverse=True)

    path = []

    def dfs(curr):
        while graph[curr]:
            next_airport = graph[curr].pop()
            dfs(next_airport)
        path.append(curr)

    dfs("ICN")

    return path[::-1]