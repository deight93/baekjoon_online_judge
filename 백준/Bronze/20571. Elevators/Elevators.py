import sys

b, n = sys.stdin.readline().rstrip().split(" ")
n = int(n)

if b == "residential":
    if n <= 1:
        print(0)
    elif 1 < n <= 5:
        print(1)
    elif 5 < n <= 10:
        print(2)
    elif 10 < n <= 15:
        print(3)
    elif 15 < n <= 20:
        print(4)
elif b == "commercial":
    if n <= 1:
        print(0)
    elif 1 < n <= 7:
        print(1)
    elif 7 < n <= 14:
        print(2)
    elif 14 < n <= 20:
        print(3)
else:
    if n <= 1:
        print(0)
    elif 1 < n <= 4:
        print(1)
    elif 4 < n <= 8:
        print(2)
    elif 8 < n <= 12:
        print(3)
    elif 12 < n <= 16:
        print(4)
    elif 16 < n <= 20:
        print(5)