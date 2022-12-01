import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    temp = " "*(n-i)
    temp += "*"*((2*i)-1)
    print(temp)