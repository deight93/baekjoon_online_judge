import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for i in range(n)]

def divide(arr):
    x = len(arr) // 2
    if x < 1:
        return arr

    r = [[] for _ in range(4)]
    for i, a in enumerate(arr):
        if i < x:
            r[0].append(a[:x])
            r[1].append(a[x:])
        else:
            r[2].append(a[:x])
            r[3].append(a[x:])
    return r

def check(arr):
    one_ck = False
    zero_ck = False

    for a in arr:
        for i in a:
            if i == '1':
                one_ck = True
            elif i == '0':
                zero_ck = True

    if one_ck and zero_ck:
        return -1
    elif one_ck:
        return '1'
    else:
        return '0'

def solve(arr):
    ck = check(arr)

    if ck != -1:
        return ck

    div_arr = divide(arr)

    return '(' + \
        solve(div_arr[0]) + \
        solve(div_arr[1]) + \
        solve(div_arr[2]) + \
        solve(div_arr[3]) + \
        ')'

print(solve(arr))