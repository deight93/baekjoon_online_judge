import sys

n = int(sys.stdin.readline().rstrip())

while True:
    n += 1
    if len(str(n)) == len(set(str(n))):
        print(n)
        break
