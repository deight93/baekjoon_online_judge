import sys

n = int(sys.stdin.readline().rstrip())

temp = [0, 1, 2]
for i in range(3, n+1):
    temp.append((temp[i-1] + temp[i-2])%15746)
print(temp[n])