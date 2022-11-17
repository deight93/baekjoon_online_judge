import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
re_input_list = input_list[::-1]

in_dp = [1 for i in range(n)]
de_dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if input_list[i]>input_list[j]:
            in_dp[i] = max(in_dp[i], in_dp[j]+1)
        if re_input_list[i]>re_input_list[j]:
            de_dp[i] = max(de_dp[i], de_dp[j]+1)

print(sum(max(list(zip(in_dp, de_dp[::-1])), key=lambda x: x[0]+x[1]))-1)