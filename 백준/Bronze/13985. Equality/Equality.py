
import sys

a = sys.stdin.readline().rstrip().split(" ")

if int(a[0])+int(a[2]) == int(a[4]):
    print("YES")
else:
    print("NO")

