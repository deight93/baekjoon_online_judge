def solution(code):
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if code[idx] == "1":
            mode += 1
            mode = mode % 2
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                if idx % 2 == 1:
                    ret += code[idx]
    
    if ret == '':
        ret = "EMPTY"
    
    return ret