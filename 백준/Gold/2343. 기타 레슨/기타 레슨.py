import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

left = max(nums)
right = sum(nums)

while left <= right:
    mid = (left + right) // 2

    cnt, total = 1, 0
    for num in nums:
        if total + num > mid:
            total = num
            cnt += 1
        else:
            total += num

    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)
