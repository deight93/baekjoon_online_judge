import sys

n = int(sys.stdin.readline())

input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]
input_list = sorted(input_list, key=lambda x: x[0])
temp = [i[1] for i in input_list]
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if temp[i] > temp[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))