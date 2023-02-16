import sys

w, h = map(int, sys.stdin.readline().rstrip().split(" "))
print(w+h - (w**2+h**2)**0.5)