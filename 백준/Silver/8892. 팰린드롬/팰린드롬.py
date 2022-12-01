import sys


def check_p(s):
    ck = True
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            ck = False

    if ck is True:
        return True
    else:
        return False


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    r = 0
    n = int(sys.stdin.readline().rstrip())
    input_list = [sys.stdin.readline().rstrip() for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            a = input_list[i] + input_list[j]
            b = input_list[j] + input_list[i]

            if check_p(a) is True:
                r = a
                break

            if check_p(b) is True:
                r = b
                break
    print(r)