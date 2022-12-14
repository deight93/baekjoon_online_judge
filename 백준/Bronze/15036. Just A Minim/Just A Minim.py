import sys

n = int(sys.stdin.readline().rstrip())
output = 0

for i in map(int, sys.stdin.readline().rstrip().split(" ")):
    if i == 0:
        output += 2
    else:
        output += 1/i

print(output)
