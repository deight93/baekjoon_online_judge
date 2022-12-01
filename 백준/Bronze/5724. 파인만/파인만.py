import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    temp = 0
    for i in range(1, n+1):
        temp += i**2
    print(temp)