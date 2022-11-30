import sys

e, s, m = map(int, sys.stdin.readline().rstrip().split(" "))

temp_e = 0
temp_s = 0
temp_m = 0
n = 0
while True:
    temp_e += 1
    temp_s += 1
    temp_m += 1
    n += 1
    if temp_e == 16:
        temp_e = 1
    if temp_s == 29:
        temp_s = 1
    if temp_m == 20:
        temp_m = 1

    if temp_e == e and temp_s == s and temp_m == m:
        break

print(n)

