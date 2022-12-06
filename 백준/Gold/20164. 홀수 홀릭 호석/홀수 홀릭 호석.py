import sys


def count_odd(str_n):
    cnt = 0
    for i in str_n:
        if int(i) % 2 != 0:
            cnt += 1
    return cnt


def len2(str_n):
    return str(int(str_n[0]) + int(str_n[1]))


def len3(str_n, i, j):
    return str(int(str_n[:i + 1]) + int(str_n[i + 1:j + 1]) + int(str_n[j + 1:]))


def calc(str_n, cnt):
    str_n_len = len(str_n)
    if str_n_len == 1:
        count_list.append(cnt)
    elif str_n_len == 2:
        new_n = len2(str_n)
        calc(new_n, cnt + count_odd(new_n))
    elif str_n_len >= 3:
        for i in range(len(str_n) - 2):
            for j in range(i + 1, len(str_n) - 1):
                new_n = len3(str_n, i, j)
                calc(new_n, cnt + count_odd(new_n))


n = sys.stdin.readline().rstrip()
count_list = []
init_cnt = count_odd(n)
calc(n, init_cnt)
print(min(count_list), max(count_list))

