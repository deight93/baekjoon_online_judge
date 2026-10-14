def solution(str_list, ex):
    join_list = [i for i in str_list if i.find(ex) < 0]
    
    answer = "".join(join_list)
    return answer