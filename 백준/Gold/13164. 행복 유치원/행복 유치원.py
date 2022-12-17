import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
a = list(map(int, sys.stdin.readline().rstrip().split(" ")))

temp = []
for i in range(n-1):
    temp.append(a[i+1]-a[i])
temp.sort(reverse=True)
print(sum(temp[k-1:]))

