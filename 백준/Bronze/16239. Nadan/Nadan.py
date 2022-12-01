
import sys

k = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())


for i in range(1, n):
    print(i)
    k -= i
print(k)

