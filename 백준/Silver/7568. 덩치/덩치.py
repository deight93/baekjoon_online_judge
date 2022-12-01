import sys

n = int(sys.stdin.readline())
x_y_list = [[int(j) for j in input().split(" ")] for i in range(n)]


temp = ""
for k, i in enumerate(x_y_list):
    cnt = 1
    for k2, j in enumerate(x_y_list):
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1

    if k != len(x_y_list)-1:
        temp += str(cnt)+" "
    else:
        temp += str(cnt)

print(temp)