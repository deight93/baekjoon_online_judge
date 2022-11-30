import sys

n, m = sys.stdin.readline().rstrip().split(" ")

total = 0
for i in n:
    for j in m:
        total += int(i)*int(j)
print(total)