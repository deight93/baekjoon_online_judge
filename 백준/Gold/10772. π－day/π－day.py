import sys


def p(n, k, cnt):
    if dp[n][k][cnt] == 0:
        if k == n:
            dp[n][k][cnt] = 1
        elif k == 1:
            dp[n][k][cnt] = 1
        else:
            t = 0
            for i in range(cnt, (int(n / k))+1):
                t = t + p(n-i, k-1, i)
            dp[n][k][cnt] = t
    return dp[n][k][cnt]


init_n = int(sys.stdin.readline().rstrip())
init_k = int(sys.stdin.readline().rstrip())

dp = [[[0 for _ in range(init_n+1)] for _ in range(init_k+1)] for _ in range(init_n+1)]
print(p(init_n, init_k, 1))
