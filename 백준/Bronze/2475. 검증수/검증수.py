import sys
n = [int(j)**2 for j in sys.stdin.readline().rstrip().split(" ")]

print(sum(n)%10)
