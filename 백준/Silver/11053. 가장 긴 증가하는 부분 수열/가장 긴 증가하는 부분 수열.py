
import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
input_list.insert(0, 0)
dp = [0, input_list[1]]

for i in range(1, n+1):
    for j in range(1, len(dp)):
        if dp[j] > input_list[i] > dp[j-1]:
            dp[j] = input_list[i]

    if input_list[i] > dp[-1]:
        dp += [input_list[i]]

print(len(dp)-1)