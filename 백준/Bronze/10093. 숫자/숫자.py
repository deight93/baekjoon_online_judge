import sys

a, b = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
temp = [str(i) for i in range(a+1, b)]
print(len(temp))
print(" ".join(temp))