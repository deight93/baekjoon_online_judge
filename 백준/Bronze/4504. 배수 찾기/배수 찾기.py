import sys

n = int(sys.stdin.readline().rstrip())
temp = []
while True:
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        break
    temp += [a]

for i in temp:
    if i % n == 0:
        print("{} is a multiple of {}.".format(i, n))
    else:
        print("{} is NOT a multiple of {}.".format(i, n))
