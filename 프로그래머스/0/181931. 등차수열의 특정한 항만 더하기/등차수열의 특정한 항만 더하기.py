def solution(a, d, included):
    answer = 0
    for i, c in enumerate(included):
        if c:
            answer += a + (d * i)
    return answer