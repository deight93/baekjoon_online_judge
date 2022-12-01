import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if round(m**0.5) == round(n**0.5):
    print(-1)
else:
    total = []
    for i in range(math.ceil(m**0.5), math.floor(n**0.5)+1):
        total += [i**2]
    print(sum(total))
    print(min(total))