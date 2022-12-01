import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    b = sys.stdin.readline().rstrip()

    temp = ""
    for i in b:
        e = (a[0] * (ord(i)-65) + a[1]) % 26
        temp += chr(e+65)
    print(temp)