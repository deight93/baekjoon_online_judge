
import sys

k = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

a = 210

for i in range(n):
    t, z = sys.stdin.readline().rstrip().split(" ")
    a -= int(t)
    if a <= 0:
        break

    if z == "T":
        k += 1
        if k > 8:
            k = 1
    else:
        pass

print(k)
