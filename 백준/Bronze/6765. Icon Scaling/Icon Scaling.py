import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    print("*"*n+"x"*n+"*"*n)
for i in range(n):
    print(" "*n+"x"*n+"x"*n)
for i in range(n):
    print("*"*n+" "*n+"*"*n)


