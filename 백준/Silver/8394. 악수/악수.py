import sys

n = int(sys.stdin.readline().rstrip())
dp = [1, 1]
for i in range(1, n):
    dp += [(dp[i]+dp[i-1])%10]

print(dp[n])