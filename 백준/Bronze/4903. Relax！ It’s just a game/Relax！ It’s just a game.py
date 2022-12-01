import math
import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    if a == -1 and b == -1:
        break
    temp = int(math.factorial(a+b)/(math.factorial(a)*math.factorial(b)))
    if temp == a+b:
        print("{}+{}={}".format(a, b, a+b))
    else:
        print("{}+{}!={}".format(a, b, a+b))

