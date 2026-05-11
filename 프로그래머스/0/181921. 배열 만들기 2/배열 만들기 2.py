def solution(l, r):
    z = "0"
    f = "5"
    answer = []
    
    for i in range(1, len(str(r))+1):
        if i == 1:
            answer.append(f)
            temp = ["5"]
        else:
            temp_copy = temp.copy()
            temp = []
            
            for t in temp_copy:
                answer.append(t+z)
                answer.append(t+f)
                temp.append(t+z)
                temp.append(t+f)
                
    
    answer = [int(i) for i in answer if l <= int(i) <= r]
    if not answer:
        answer = [-1]
            
    return answer