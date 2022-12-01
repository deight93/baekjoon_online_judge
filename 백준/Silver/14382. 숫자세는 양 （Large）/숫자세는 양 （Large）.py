import sys

t = int(sys.stdin.readline().rstrip())
temp = [i for i in "0123456789"]

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print("Case #{}: INSOMNIA".format(i+1))
    else:
        c = 0
        c_temp = []
        while True:
            c += 1
            for j in str(c*n):
                c_temp.append(j)
            c_temp = sorted(list(set(c_temp)))

            if temp == c_temp:
                break
        print("Case #{}: {}".format(i + 1, c*n))

