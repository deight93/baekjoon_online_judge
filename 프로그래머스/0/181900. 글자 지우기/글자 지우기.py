def solution(my_string, indices):
    my_string = [[i, 0] for i in my_string]
    for i in indices:
        my_string[i][1] = 1
    
    return "".join([i[0] for i in my_string if i[1] == 0])