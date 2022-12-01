
import sys
import math

n = int(sys.stdin.readline().rstrip())
a_i = map(int, sys.stdin.readline().rstrip().split(" "))
b, c = map(int, sys.stdin.readline().rstrip().split(" "))

t = 0
for a in a_i:
    if math.ceil((a-b)/c) >= 1:
        t += 1+math.ceil((a-b)/c)
    else:
        t += 1
print(t)

