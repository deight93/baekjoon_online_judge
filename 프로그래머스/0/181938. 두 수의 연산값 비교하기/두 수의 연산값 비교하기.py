def solution(a, b):
    answer = 2 * a * b
    if int(str(a)+str(b)) >= answer:
        answer = int(str(a)+str(b))
        
    return answer