import sys
import math

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
print(" ".join([str(math.ceil(((a*b)*i)/100.0)) for i in range(10, 91, 10)]))
