import sys

c = sys.stdin.readline()

k = [int(i) for i in c[:-1]]
k.sort(reverse=True)
a = ""
for i in k:
    a += str(i)
print(a)