import sys

n = int(sys.stdin.readline().rstrip())
ff = [[1, 3], [1, 4], [3, 4]]
f = sorted([sorted(list(map(int, sys.stdin.readline().rstrip().split(" ")))) for _ in range(n)])

if f == ff:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")

