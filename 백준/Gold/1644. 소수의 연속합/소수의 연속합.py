import sys

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n**0.5+1)):
        if arr[i]:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    return arr


n = int(sys.stdin.readline().rstrip())
arr = is_prime_num(n)
n_p_l = []
for i in range(len(arr)):
    if arr[i]:
        n_p_l += [i]

cnt = 0
for i in range(len(n_p_l)):
    for j in range(i+1, len(n_p_l)+1):
        sum_npl = sum(n_p_l[i:j])
        if sum_npl == n:
            cnt += 1
        elif sum_npl > n:
            break
print(cnt)