import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip().split(" ")
m = int(sys.stdin.readline())
temp = sys.stdin.readline().rstrip().split(" ")
temp2 = set(temp)-set(a)

for i in temp:
    if i in temp2:
        print(0)
    else:
        print(1)
