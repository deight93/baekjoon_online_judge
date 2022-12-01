
import sys


while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    temp = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            temp += [i]

    if sum(temp) == n:
        temp1 = "{} = ".format(n)
        for k, j in enumerate(temp):
            if k == len(temp)-1:
                temp1 = temp1 + str(j)
            else:
                temp1 = temp1+str(j)+" + "
        print(temp1)
    else:
        print("{} is NOT perfect.".format(n))