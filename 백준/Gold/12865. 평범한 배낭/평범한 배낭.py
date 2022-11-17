import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = map(int, input_list[i - 1])
    for j in range(1, k+1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])