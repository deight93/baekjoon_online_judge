import sys
import fractions

n = int(sys.stdin.readline().rstrip())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

for i in range(1, n):
    print("{}/{}".format(fractions.Fraction(input_list[0], input_list[i]).numerator,
                         fractions.Fraction(input_list[0], input_list[i]).denominator))