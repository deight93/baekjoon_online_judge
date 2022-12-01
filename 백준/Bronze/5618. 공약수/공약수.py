
import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

divs = []
for i in input_list:
    temp = []
    for j in range(1, int(i**0.5)+1):
        if i%j == 0:
            temp += [j]
            if j != i // j:
                temp += [i//j]

    divs.append(set(temp))

comdiv = set.intersection(*divs)
[print(i) for i in sorted(comdiv)]