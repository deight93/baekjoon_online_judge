import sys

n = sys.stdin.readline().rstrip()
len_n = int(len(n)/2)
n1 = sum([int(i) for i in n[:len_n]])
n2 = sum([int(i) for i in n[len_n:]])

if n1 == n2:
    print("LUCKY")
else:
    print("READY")

