import sys

n, s = map(int, sys.stdin.readline().rstrip().split(" "))
nm = [s*i for i in map(int, sys.stdin.readline().rstrip().split(" "))]
if max(nm) % 1000 == 0:
    print(max(nm)//1000)
else:
    print((max(nm)//1000)+1)

