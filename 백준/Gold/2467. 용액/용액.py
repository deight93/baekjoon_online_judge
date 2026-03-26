import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

l, r = 0, n - 1
s = abs(nums[l]+nums[r])
a, b = nums[l], nums[r]

while l < r:
    temp = nums[l]+nums[r]
    abs_temp = abs(temp)
    if abs_temp < s:
        s = abs_temp
        a, b = nums[l], nums[r]

    if temp < 0:
        l += 1
    else:
        r -= 1

print(a, b)