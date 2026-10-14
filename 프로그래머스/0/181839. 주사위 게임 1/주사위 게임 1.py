def solution(a, b):
    a_r = a % 2
    b_r = b % 2
    
    if a_r + b_r == 1:
        answer = 2*(a+b)
    elif a_r + b_r == 2:
        answer = a**2 + b**2
    else:
        answer = abs(a-b)
        
    return answer