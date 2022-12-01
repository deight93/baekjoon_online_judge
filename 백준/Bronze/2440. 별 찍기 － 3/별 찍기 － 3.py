
import sys

n = int(sys.stdin.readline().rstrip())

a = ["*"*i for i in range(1, n+1)]
[print(i) for i in a[::-1]]