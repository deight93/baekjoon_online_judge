def solution(my_string, is_suffix):
    sufixs = []
    for i in range(len(my_string)):
        sufixs.append(my_string[i:])
    
    return 1 if is_suffix in sufixs else 0