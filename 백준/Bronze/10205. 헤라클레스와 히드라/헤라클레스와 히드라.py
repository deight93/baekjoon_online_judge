
import sys

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()

    for i in s:
        if i == "c":
            a = 1
        else:
            a = -1
        n += a

        if n == 0:
            break
    print("Data Set {}:".format(_+1))
    print(n)

    if _ != k-1:
        print()