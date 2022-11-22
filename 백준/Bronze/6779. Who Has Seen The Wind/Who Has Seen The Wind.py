import sys

h = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

ck = 1
for t in range(1, m):
    A = (-6)*(t**4) + h*(t**3) + 2*(t**2) + t
    if A <= 0:
        print("The balloon first touches ground at hour: {}".format(t))
        ck = 0
        break

if ck == 1:
    print("The balloon does not touch ground in the given time.")


