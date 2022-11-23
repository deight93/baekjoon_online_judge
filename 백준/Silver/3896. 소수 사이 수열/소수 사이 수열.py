
import sys

n = 1299709
a = [False, False] + [True] * (n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    for k, i in enumerate(primes):
        if i > n:
            print(primes[k]-primes[k-1])
            break
        elif i == n:
            print(0)
            break
