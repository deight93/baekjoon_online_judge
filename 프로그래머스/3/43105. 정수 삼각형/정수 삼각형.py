def solution(triangle):
    answer = 0

    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i])-1):
            triangle[i-1][j] = triangle[i-1][j] + max(triangle[i][j], triangle[i][j+1])
            answer = triangle[i-1][j]

    return answer