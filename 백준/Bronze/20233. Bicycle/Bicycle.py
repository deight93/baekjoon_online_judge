import sys

a = int(sys.stdin.readline().rstrip())
x = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
y = int(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline().rstrip())

ar = 0
br = 0
if t-30 > 0:
    ar = t-30

if t-45 > 0:
    br = t-45
print(a+((ar*x)*21), b+((br*y)*21))