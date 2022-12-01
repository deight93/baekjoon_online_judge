
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    if n == 1:
        print("#" * n)
    else:
        for i in range(n):
            if i == 0:
                print("#" * n)
            elif i == n-1:
                a = "#"
                print("#" * n)
            else:
                temp = ""
                for j in range(n):
                    if j == 0:
                        temp += "#"
                    elif j == n - 1:
                        temp += "#"
                    else:
                        temp += "J"
                print(temp)
    print()