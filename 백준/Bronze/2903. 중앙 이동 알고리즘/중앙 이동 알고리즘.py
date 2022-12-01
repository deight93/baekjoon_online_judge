import sys

n = int(sys.stdin.readline().rstrip())

temp = [2]
for i in range(n):
    temp.append(temp[i]+temp[i]-1)

print(temp[-1]**2)