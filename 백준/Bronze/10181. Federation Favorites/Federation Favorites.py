import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    if int(n/2) == n/2:
        temp = []
        for i in range(1, int(n/2)+1):
            if n % i == 0:
                temp += [i]
        if sum(temp) == n:
            p = "{} = ".format(n)
            print(p+" + ".join([str(i) for i in temp]))
        else:
            print("{} is NOT perfect.".format(n))
    else:
        print("{} is NOT perfect.".format(n))

