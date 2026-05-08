def solution(arr, queries):    
    answer = []
    for q in queries:
        s = q[0]
        e = q[1]
        k = q[2]
        r = [a for a in arr[s:e+1] if a > k]
        
        if not r:
            answer.append(-1)
        else:
            answer.append(min(r))
    return answer        
        
        
