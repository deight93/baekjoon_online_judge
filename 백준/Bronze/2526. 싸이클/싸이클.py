
import sys

n, p = map(int, sys.stdin.readline().rstrip().split(" "))

temp = []
n2 = n
while True:
    if temp.count(n2) >= 3:
        break
    else:
        temp.append(n2)
        n2 = ((n*n2) % p)

temp2 = []
for i in temp:
    if temp.count(i) == 1:
        temp2.append(i)

print(len(set(temp)-set(temp2)))