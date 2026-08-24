def solution(arr, n):
    for i in range(1 - (len(arr) % 2), len(arr), 2):
        arr[i] += n

    return arr