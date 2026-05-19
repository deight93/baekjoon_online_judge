def solution(my_string, queries):

    my_string = list(my_string)
    for q in queries:
        a = my_string[q[0]:q[1]+1]
        a.reverse()
        my_string[q[0]:q[1]+1] = a
    answer = ''.join(my_string)

    return answer