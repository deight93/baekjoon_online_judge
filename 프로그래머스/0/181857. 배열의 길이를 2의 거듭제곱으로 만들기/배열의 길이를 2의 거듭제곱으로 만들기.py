
def solution(arr):
    s = 1
    
    while s < len(arr):
        s *= 2
        
    result = arr + [0] * (s - len(arr))
    return result
