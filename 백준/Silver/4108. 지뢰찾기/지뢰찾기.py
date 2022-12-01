import sys

while True:
    r, c = map(int, sys.stdin.readline().rstrip().split(" "))
    if r == 0 and c == 0 :
        break

    l = [list(sys.stdin.readline().rstrip().replace(".", "0")) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if l[i][j] == "*":
                for ii in range(0 if i-1 < 0 else i-1, r if i+2 > r else i+2):
                    for jj in range(0 if j - 1 < 0 else j - 1, c if j + 2 > c else j + 2):
                        if (i == ii and j == jj) or l[ii][jj] == "*":
                            pass
                        else:
                            a = int(l[ii][jj])+1
                            l[ii][jj] = str(a)

    for i in l:
        print("".join(i))

