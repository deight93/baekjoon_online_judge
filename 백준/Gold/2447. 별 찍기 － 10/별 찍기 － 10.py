import sys

n = int(sys.stdin.readline())


def factorial(n):
    if n == 1:
        return ["*"]

    a = factorial(int(n/3))

    temp = []
    for i in a:
        temp += [i*3]
    for i in a:
        temp += [i+" "*int(n/3)+i]
    for i in a:
        temp += [i*3]

    return temp

k = factorial(n)

for i in k:
    print(i)