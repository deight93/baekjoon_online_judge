
import sys

a = 1000001
sieve = [True] * a

m = int(a ** 0.5)
for i in range(2, m + 1):
    if sieve[i] is True:
        for j in range(i+i, a, i):
            sieve[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    for i in range(3, len(sieve)):
        if sieve[i] and sieve[n-i]:
            print("{} = {} + {}".format(i + (n-i), i, n-i))
            break