import sys

t = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(t)]
n = max(input_list)

a = [1, 1, 2, 4]

for i in range(4, n+1):
    a.append(a[i-1]+a[i-2]+a[i-3]+a[i-4])

for i in input_list:
    print(a[i])