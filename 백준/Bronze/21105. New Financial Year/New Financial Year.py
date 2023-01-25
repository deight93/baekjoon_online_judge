import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    p, c = map(float, sys.stdin.readline().rstrip().split(" "))
    print(p/(c+100)*100)