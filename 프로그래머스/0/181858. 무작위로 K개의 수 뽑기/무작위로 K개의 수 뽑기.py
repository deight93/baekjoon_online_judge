def solution(arr, k):
    answer = [-1] * k
    t = 0
    
    for i in arr:
        if i not in answer and t < k:
            answer[t] = i
            t += 1
    
    return answer