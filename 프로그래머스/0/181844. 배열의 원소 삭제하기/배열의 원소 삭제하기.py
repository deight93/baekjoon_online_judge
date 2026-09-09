def solution(arr, delete_list):
    answer = []
    delete_set = set(delete_list)
    for i in arr:
        if i not in delete_set:
            answer.append(i)
    return answer