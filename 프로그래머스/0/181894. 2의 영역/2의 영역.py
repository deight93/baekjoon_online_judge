def solution(arr):
    answer = [-1]
    start = 0
    end = 0
    ck = False
    
    for i, v in enumerate(arr):
        if v == 2:
            start = i
            ck = True
            break
    for i, v in enumerate(arr[::-1]):
        if v == 2:
            end = len(arr) - i
            ck = True
            break
    
    if ck:
        answer = arr[start:end]

    return answer