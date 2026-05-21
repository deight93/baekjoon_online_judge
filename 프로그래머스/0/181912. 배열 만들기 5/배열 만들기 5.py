def solution(intStrs, k, s, l):
    answer = []
    
    for iss in intStrs:
        if k < int(iss[s:s+l]):
            answer.append(int(iss[s:s+l]))
    return answer