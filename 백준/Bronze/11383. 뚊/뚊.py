
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list1 = [sys.stdin.readline().rstrip() for _ in range(n)]
input_list2 = [sys.stdin.readline().rstrip() for _ in range(n)]

a = [i*2 for i in input_list1[0]]

ck = True
for i in range(n):
    if input_list2[i] != "".join([i*2 for i in input_list1[i]]):
        ck = False
        break

if ck is True:
    print("Eyfa")
else:
    print("Not Eyfa")
