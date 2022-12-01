import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    temp = " "*i
    temp += "*"*(n-i)
    print(temp)