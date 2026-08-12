def solution(strArr):
    len_dict = {}
    
    for s in strArr:
        if len(s) in len_dict:
            len_dict[len(s)].append(s)
        else:
            len_dict[len(s)] = [s]
    
    return len(max(len_dict.values(), key=lambda x: len(x)))