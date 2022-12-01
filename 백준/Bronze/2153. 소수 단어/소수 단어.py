import sys

s = sys.stdin.readline().rstrip()

temp = 0
for i in s:
    if i.isupper():
        temp += (ord(i)-38)
    else:
        temp += (ord(i)-96)

ck = True
for i in range(2, int(temp**0.5)+1):
    if temp % i == 0:
        ck = False
        break

if ck is True:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
