import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]
dp = [0 for _ in range(n)]

if n == 1:
    dp[0] = input_list[0]
elif n == 2:
    dp[0] = input_list[0]
    dp[1] = input_list[0]+input_list[1]
else:
    dp[0] = input_list[0]
    dp[1] = input_list[0] + input_list[1]
    dp[2] = max(input_list[1] + input_list[2], input_list[0] + input_list[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-3]+input_list[i-1] + input_list[i], input_list[i]+dp[i-2], dp[i-1])

print(dp[n-1])