import sys
import math


n = int(sys.stdin.readline())

for i in range(n):
    input_list = [int(i) for i in sys.stdin.readline().split()]
    a = input_list[0]
    b = input_list[1]
    temp = (a * b) // math.gcd(a,b)
    print(temp)
