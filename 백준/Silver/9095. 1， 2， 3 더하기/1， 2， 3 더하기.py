import sys

t = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for i in range(t)]

dp = [1, 2, 4]
for i in range(3, 12):
    dp += [dp[i-3]+dp[i-2]+dp[i-1]]

for i in input_list:
    print(dp[i-1])