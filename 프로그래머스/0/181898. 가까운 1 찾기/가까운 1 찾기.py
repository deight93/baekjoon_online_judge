def solution(arr, idx):
    
    find_one_arr = arr[idx:]
    answer = -1
    
    for i, v in enumerate(find_one_arr):
        if v == 1:
            answer = i + idx
            break
    
    return answer