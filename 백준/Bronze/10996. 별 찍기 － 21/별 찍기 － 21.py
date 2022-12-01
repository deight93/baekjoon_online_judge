import sys

n = int(sys.stdin.readline().rstrip())
if n != 1:
    n = n*2
    for i in range(n):
        temp = ""
        if i % 2 == 0:
            for j in range(n // 2):
                if j % 2 == 0:
                    temp += "*"
                else:
                    temp += " "
        else:
            for j in range(n // 2):
                if j % 2 == 0:
                    temp += " "
                else:
                    temp += "*"
        print(temp)
else:
    temp = "*"
    print(temp)
