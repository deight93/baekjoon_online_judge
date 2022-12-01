
import sys

n = int(sys.stdin.readline())

dp = [0, 1]
for i in range(0, n):
    dp.append(dp[i]+dp[i+1])

print(dp[n])