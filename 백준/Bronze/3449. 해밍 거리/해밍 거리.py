import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    temp = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            temp += 1
    print("Hamming distance is {}.".format(temp))