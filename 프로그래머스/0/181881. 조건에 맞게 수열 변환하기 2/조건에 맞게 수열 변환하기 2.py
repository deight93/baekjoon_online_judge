def solution(arr):
    cnt = 0
    
    while True:
        temp_arr = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                temp_arr.append(i // 2)
            elif i < 50 and i % 2 == 1:
                temp_arr.append((i * 2) + 1)
            else:
                temp_arr.append(i)
        if arr == temp_arr:
            break
        else:
            cnt += 1
            arr = temp_arr
    
    return cnt