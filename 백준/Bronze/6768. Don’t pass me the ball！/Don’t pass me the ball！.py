import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
nums = [i for i in range(n-1)]
r = list(combinations(nums, 3))
print(len(r))


