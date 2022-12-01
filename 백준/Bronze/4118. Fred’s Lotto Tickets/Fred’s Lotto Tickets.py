import sys


while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        n_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]
        n_list = set([j for i in n_list for j in i])

        ck = True
        for i in range(1, 50):
            if str(i) not in n_list:
                ck = False
                break
        if ck:
            print("Yes")
        else:
            print("No")

