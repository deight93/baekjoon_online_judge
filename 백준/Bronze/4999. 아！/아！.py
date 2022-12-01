import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

if len(b) <= len(a):
    print("go")
else:
    print("no")