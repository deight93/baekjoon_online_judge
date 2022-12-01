import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))

    if a == 0 and b == 0:
        break
    else:
        if (a-b) % 2 == 0:
            print((a-b)//2, 0)
        if (a-b) % 2 == 1:
            if (a-b)//2 == 0:
                print((a-b)//2, 0)
            else:
                print(((a - b) // 2)-1, 1)


