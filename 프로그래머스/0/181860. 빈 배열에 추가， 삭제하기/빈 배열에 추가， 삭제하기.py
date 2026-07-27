def solution(arr, flag):
    answer = []
    
    for i, v in enumerate(flag):
        if v:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
        
    return answer