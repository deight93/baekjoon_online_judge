import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

if m <= 2:
    print("NEWBIE!")
else:
    if m <= n:
        print("OLDBIE!")
    else:
        print("TLE!")