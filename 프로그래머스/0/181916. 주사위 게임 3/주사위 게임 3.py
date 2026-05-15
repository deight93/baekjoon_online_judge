def solution(a, b, c, d):
    list_abcd = [a, b, c, d]
    set_abcd = set(list_abcd)
    list_set_abcd = list(set_abcd)

    if len(set_abcd) == 1:
        answer = 1111*list_set_abcd[0]
    elif len(set_abcd) == 2:
        if list_abcd.count(list_set_abcd[0]) == 1:
            q = list_set_abcd[0]
            p = list_set_abcd[1]
            answer = (10*p+q)**2
        elif list_abcd.count(list_set_abcd[0]) == 3:
            q = list_set_abcd[1]
            p = list_set_abcd[0]
            answer = (10*p+q)**2
        else:
            answer = (list_set_abcd[0]+list_set_abcd[1]) * abs(list_set_abcd[0]-list_set_abcd[1])
    elif len(set_abcd) == 3:
        temp = []
        for i in range(len(list_set_abcd)):
            if list_abcd.count(list_set_abcd[i]) == 2:
                continue
            else:
                temp.append(list_set_abcd[i])
        answer = temp[0] * temp[1]
    else:
        answer = min(list_abcd)

    return answer