def solution(strArr):
    answer = [s for s in strArr if s.find("ad") == -1]
    return answer