import sys

k, n = map(int, sys.stdin.readline().rstrip().split(" "))
lan = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

left = 1
right = max(lan)
r_ck = 0
while left <= right:
    mid = (left + right) // 2
    ck = 0
    for i in lan:
        ck += (i//mid)

    if ck >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)

