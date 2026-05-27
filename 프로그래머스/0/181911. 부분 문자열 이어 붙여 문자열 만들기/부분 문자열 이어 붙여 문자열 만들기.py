def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(my_strings)):
        s = my_strings[i]
        p = parts[i]
        
        answer += s[p[0]:p[1]+1]
    
    return answer