import sys

n = int(sys.stdin.readline().rstrip())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

dp = [0 for _ in range(n)]
dp[0] = input_list[0]

for i in range(1, n):
    dp[i] = max(input_list[i], dp[i - 1] + input_list[i])

print(max(dp))
