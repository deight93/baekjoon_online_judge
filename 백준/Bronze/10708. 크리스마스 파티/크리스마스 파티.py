import sys


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
a_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
s = [0] * n

for a in a_list:
    b_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    f = n - b_list.count(a)
    for i, b in enumerate(b_list):
        if a == b:
            if a == i+1:
                s[i] += 1+f
            else:
                s[i] += 1

for i in s:
    print(i)

