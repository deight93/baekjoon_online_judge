
import sys

dp = [1, 1, 2]
for i in range(3, 31):
    temp = 0
    for j in range(i):
        temp += dp[j] * dp[i-1-j]
    dp.append(temp)

for _ in range(1000):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    print(dp[n])