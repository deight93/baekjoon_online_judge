
import sys

a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
b = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(min(a[0]+b[1], a[1]+b[0]))