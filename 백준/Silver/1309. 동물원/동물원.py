import sys

n = int(sys.stdin.readline().rstrip())
dp = [1, 3]
for i in range(1, n):
    dp += [(dp[i]*2+dp[i-1]) % 9901]

print(dp[-1])