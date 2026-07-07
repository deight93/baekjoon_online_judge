def solution(myString, pat):
    answer = myString.lower().find(pat.lower())
    if answer == -1:
        return 0
    else:
        return 1
