import sys


p, k = map(int, sys.stdin.readline().rstrip().split(" "))

nums = [False, False] + [True] * (k-2)
for i in range(2, int(k**0.5) + 1):
    if nums[i] is True:
        for j in range(i+i, k, i):
            nums[j] = False

ck = True
for i in range(2, k):
    if nums[i] is True:
        if p % i == 0:
            ck = False

            break

if ck is True:
    print("GOOD")
else:
    print("BAD {}".format(i))

