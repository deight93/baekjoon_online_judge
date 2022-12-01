import sys

n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().rstrip().split(" ")))
p = sys.stdin.readline().rstrip()

p_list = []
for i in p:
    if i.isupper():
        p_list += [ord(i)-64]
    elif i.islower():
        p_list += [ord(i)-70]
    else:
        p_list += [0]


if sorted(s) == sorted(p_list):
    print('y')
else:
    print('n')

