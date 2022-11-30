
import sys
import itertools
import math

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

temp = []
for i in itertools.combinations(input_list, 3):
    lcm1 = i[0] * i[1]//math.gcd(i[0], i[1])
    lcm2 = i[2] * lcm1//math.gcd(i[2], lcm1)
    temp += [lcm2]
print(min(temp))
