
import sys

n = int(sys.stdin.readline().rstrip())

temp2 = []
for i in range(1, n+1):
    temp = " "*(n-i)
    temp += "*"*((2*i)-1)
    temp2 += [temp]

for j in temp2[::-1]:
    print(j)