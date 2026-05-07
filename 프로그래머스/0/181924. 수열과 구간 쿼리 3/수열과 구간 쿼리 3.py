def solution(arr, queries):
    for q in queries:
        i = q[0]
        j = q[1]
        
        f = arr[i]
        b = arr[j]
        
        arr[i] = b
        arr[j] = f
    
    return arr