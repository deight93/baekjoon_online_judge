def solution(numLog):
    answer = ''
    for i, n in enumerate(numLog):
        if i == 0: continue
        
        m = numLog[i] - numLog[i-1]
        if m == 1:
            answer += 'w'
        elif m == -1:
            answer += 's'
        elif m == 10:
            answer += 'd'
        elif m == -10:
            answer += 'a'
        
    return answer