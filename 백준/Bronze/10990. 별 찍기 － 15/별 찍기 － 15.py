
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    temp = ""
    temp += " "*(n-i)
    temp += "*"
    temp += " " * (2*(i-1) - 1)
    if i != 1:
        temp += "*"

    print(temp)