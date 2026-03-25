import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

r = nums[0]
cnt = 0
ck = 0
if r == m:
    cnt += 1

for i in range(1, n):
    r += nums[i]
    if r < m:
        continue
    elif r == m:
        cnt += 1
        continue
    else:
        for j in range(ck, i):
            r -= nums[j]
            ck += 1
            if r < m:
                break
            elif r == m:
                cnt += 1
                break
print(cnt)