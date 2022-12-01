import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

cnt = 0
for i in range(n):
    temp = ""
    for j in range(m):
        cnt += 1
        if j == m-1:
            temp += "{}".format(cnt)
        else:
            temp += "{} ".format(cnt)
    print(temp)
