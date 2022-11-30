import sys

c1 = [i**3 for i in range(54)]
c2 = [(i*(i+1)*(i+2))/6 for i in range(96)]
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        m = 0
        for i in c1:
            for j in c2:
                if n >= i+j:
                    if m < i+j:
                        m = i+j
        print(int(m))



