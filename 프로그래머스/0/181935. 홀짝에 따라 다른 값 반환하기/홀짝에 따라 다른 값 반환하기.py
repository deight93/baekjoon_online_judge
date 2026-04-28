def solution(n):
    a = n // 2
    if n % 2 == 1:
        answer = 1
        for i in range(1, a+1):
            answer += (i*2)+1
    else:
        answer = 0
        for i in range(1, a+1):
            answer += (i*2)**2

    return answer