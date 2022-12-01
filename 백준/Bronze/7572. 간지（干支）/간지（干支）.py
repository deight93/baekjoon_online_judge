import sys

a = [str(i) for i in range(10)]
b = [chr(i) for i in range(65, 77)]

n = int(sys.stdin.readline().rstrip())-1984

print(b[abs(n%12)]+a[abs(n%10)])