import sys

n = int(sys.stdin.readline().rstrip())
print(round(n, -1*(len(str(n))-1)))

