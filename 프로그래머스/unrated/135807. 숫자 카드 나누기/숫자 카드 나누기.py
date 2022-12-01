from math import gcd


def solution(arrayA, arrayB):
    gcd1, gcd2 = arrayA[0], arrayB[0]

    for i1, i2 in zip(arrayA[1:], arrayB[1:]):
        gcd1 = gcd(i1, gcd1)
        gcd2 = gcd(i2, gcd2)

    for i in arrayB:
        if gcd1 == 1:
            break
        elif i % gcd1 == 0:
            gcd1 = 1  
            break

    for i in arrayA:
        if gcd2 == 1:
            break
        elif i % gcd2 == 0:
            gcd2 = 1
            break

    if gcd1 == 1 and gcd2 == 1:
        return 0
    else:
        return max(gcd1, gcd2)