import sys

a = int(sys.stdin.readline().rstrip())/100
b = int(sys.stdin.readline().rstrip())/100

# 에라토스테네스의 체
n = 19
temp = [False, False] + [True] * (n-1)
primes = []
for i in range(2, n+1):
    if temp[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            temp[j] = False

# dp 경우의수 4개
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
result = 0

dp[1][0][0] = (1 - a) * (1 - b)  # 다못넣음
dp[1][0][1] = (1 - a) * b  # b가 넣음
dp[1][1][0] = a * (1 - b)  # a가 넣음
dp[1][1][1] = a * b  # 둘다 넣음

for i in range(2, n):
    for j in range(i+1):
        for k in range(i+1):
            dp[i][j][k] += dp[i - 1][j][k] * (1-a) * (1-b)
            if j > 0:
                dp[i][j][k] += dp[i - 1][j - 1][k] * a * (1 - b)
            if k > 0:
                dp[i][j][k] += dp[i - 1][j][k - 1] * (1 - a) * b
            if j > 0 and k > 0:
                dp[i][j][k] += dp[i - 1][j - 1][k - 1] * a * b

# 소수 확인
for i in range(n):
    for j in range(n):
        if i in primes or j in primes:
            result += dp[18][i][j]

print(result)
