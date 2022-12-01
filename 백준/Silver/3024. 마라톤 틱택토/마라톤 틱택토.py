import sys

n = int(sys.stdin.readline().rstrip())
t_list = [sys.stdin.readline().rstrip() for _ in range(n)]

if n < 3:
    print("ongoing")
else:
    ck = True
    for i in range(n):
        if ck is True:
            for j in range(n):
                if t_list[i][j] == '.':
                    continue

                if i + 1 < n and i + 2 < n:
                    if t_list[i][j] == t_list[i + 1][j] and t_list[i][j] == t_list[i + 2][j]:
                        print(t_list[i][j])
                        ck = False
                        break

                if j + 1 < n and j + 2 < n:
                    if t_list[i][j] == t_list[i][j + 1] and t_list[i][j] == t_list[i][j + 2]:
                        print(t_list[i][j])
                        ck = False
                        break

                if i + 1 < n and i + 2 < n and j + 1 < n and j + 2 < n:
                    if t_list[i][j] == t_list[i + 1][j + 1] and t_list[i][j] == t_list[i + 2][j + 2]:
                        print(t_list[i][j])
                        ck = False
                        break

                if i + 1 < n and i + 2 < n and j - 1 >= 0 and j - 2 >= 0:
                    if t_list[i][j] == t_list[i + 1][j - 1] and t_list[i][j] == t_list[i + 2][j - 2]:
                        print(t_list[i][j])
                        ck = False
                        break

    if ck is True:
        print("ongoing")