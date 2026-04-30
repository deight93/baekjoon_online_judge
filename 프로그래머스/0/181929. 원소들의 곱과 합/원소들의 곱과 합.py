def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    
    sum_sq = sum(num_list)**2
    
    if mul < sum_sq:
        answer = 1
    else:
        answer = 0
    return answer