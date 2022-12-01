import sys

n = [i for i in sys.stdin.readline().rstrip().split(" ") if i.count("-") == 0 and i != "0"]
print(len(n))
