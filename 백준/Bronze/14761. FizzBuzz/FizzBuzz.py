import sys

x, y, n = map(int, sys.stdin.readline().rstrip().split(" "))

for i in range(1, n+1):
    temp = []
    ck = 0
    if i % x == 0:
        temp += ["Fizz"]
        ck = 1
    if i % y == 0:
        temp += ["Buzz"]
        ck = 1

    if ck == 0:
        temp = [str(i)]
    print("".join(temp))




