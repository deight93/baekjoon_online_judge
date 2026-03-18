n, k = map(int, input().split())
nums = list(map(int, input().split()))

temp = sum(nums[:k])
r = temp
for i in range(k, n):
    temp += nums[i] - nums[i-k]
    r = max(r, temp)
print(r)