def solution(myString):
    answer = ''
    
    myString = myString.lower()
    for s in myString:
        if s == "a":
            s = "A"
        answer += s
    return answer