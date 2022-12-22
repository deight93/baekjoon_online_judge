import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip().split(" ")

for i in b:
    a = a.replace(i, i.lower())
print(a)

