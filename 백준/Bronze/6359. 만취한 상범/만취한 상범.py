import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_n = int(sys.stdin.readline().rstrip())

    temp = []
    for j in range(1, input_n+1):
        for k in range(1, input_n + 1):
            a = j*k
            if a > input_n:
                break
            else:
                if j*k in temp:
                    temp.remove(j*k)
                else:
                    temp.append(j*k)

    print(len(temp))