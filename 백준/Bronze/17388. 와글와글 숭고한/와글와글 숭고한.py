
import sys

s, k, h = map(int, sys.stdin.readline().rstrip().split(" "))

if s+k+h >= 100:
    print("OK")
else:
    if min(s, k, h) == s:
        print("Soongsil")
    elif min(s, k, h) == k:
        print("Korea")
    else:
        print("Hanyang")

