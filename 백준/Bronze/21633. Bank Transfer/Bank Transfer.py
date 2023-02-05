import sys

n = int(sys.stdin.readline().rstrip())
c = 25 + (n*0.01)

if c < 100:
    print(100)
elif c > 2000:
    print(2000)
else:
    print(c)

