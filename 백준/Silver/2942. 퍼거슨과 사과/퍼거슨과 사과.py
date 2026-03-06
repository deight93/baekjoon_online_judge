
R, G = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = gcd(R, G)

for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        print(i, R // i, G // i)
        if n // i != i:
            j = n // i
            print(j, R // j, G // j)
