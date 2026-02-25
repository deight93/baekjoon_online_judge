def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(idx):
        visited[idx] = True
        for i in range(n):
            if computers[idx][i] == 1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer