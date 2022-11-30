import sys

d, h, w = map(int, sys.stdin.readline().rstrip().split(" "))
x = (d**2/(h**2+w**2))**0.5
print(int(x*h), int(x*w))


