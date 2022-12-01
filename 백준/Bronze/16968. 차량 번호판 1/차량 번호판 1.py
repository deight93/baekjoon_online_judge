
import sys

n = sys.stdin.readline().rstrip()

temp = 10 if n[0] == "d" else 26

for i in range(1, len(n)):
    if n[i] == "d":
        if n[i] == n[i-1]:
            temp *= 9
        else:
            temp *= 10
    else:
        if n[i] == n[i - 1]:
            temp *= 25
        else:
            temp *= 26

print(temp)

