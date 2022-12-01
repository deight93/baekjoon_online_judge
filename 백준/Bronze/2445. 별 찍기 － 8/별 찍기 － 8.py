import sys

n = int(sys.stdin.readline().rstrip())

temp2 = []
for i in range(1, n+1):
    temp = "*"*i
    temp += " "*(n-i)
    temp += " " * (n - i)
    temp += "*"*i
    temp2 += [temp]


for j in temp2[:n-1]:
    print(j)

for j in temp2[::-1]:
    print(j)
