def solution(myString, pat):
    answer = 0
    cs = ''
    for s in myString:
        if s == "A":
            cs += "B"
        else:
            cs += "A"
    if cs.find(pat) != -1:
        return 1
    else:
        return 0
