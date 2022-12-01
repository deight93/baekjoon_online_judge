
import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    print("Case {}:".format(i+1))
    for j in range(m):
        a = int(sys.stdin.readline().rstrip())
        if 0 <= a < 6:
            print(a+1)


