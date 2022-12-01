
import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(" ")
    s_a = sorted(a)
    s_b = sorted(b)
    if s_a == s_b:
        print("{} & {} are anagrams.".format(a, b))
    else:
        print("{} & {} are NOT anagrams.".format(a, b))