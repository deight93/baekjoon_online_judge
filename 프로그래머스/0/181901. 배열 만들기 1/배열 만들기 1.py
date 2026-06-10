def solution(n, k):
    a = n // k
    
    answer = [i * k for i in range(1, a+1)]
    return answer