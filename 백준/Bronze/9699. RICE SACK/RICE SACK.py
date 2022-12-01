
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    print("Case #{}: {}".format(_+1, max(list(map(int, sys.stdin.readline().rstrip().split(" "))))))

