import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):

    a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))

    if a + b == c:

        print("Possible")

    elif a * b == c:

        print("Possible")

    elif a - b == c or b - a == c:

        print("Possible")

    elif a / b == c or b / a == c:

        print("Possible")

    else:

        print("Impossible")

