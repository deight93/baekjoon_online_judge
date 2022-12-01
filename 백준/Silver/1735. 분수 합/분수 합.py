
import sys
import fractions

n1, d1 = map(int, sys.stdin.readline().rstrip().split(" "))
n2, d2 = map(int, sys.stdin.readline().rstrip().split(" "))

a = fractions.Fraction(n1, d1)+fractions.Fraction(n2, d2)

print(a.numerator, a.denominator)