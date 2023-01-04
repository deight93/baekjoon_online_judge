import sys

t = sys.stdin.readline().rstrip().split(" ")
temp = []
for i in t:
    if "tapioka" != i and "bubble" != i:
        temp.append(i)

if temp:
    print(" ".join(temp))
else:
    print("nothing")
#