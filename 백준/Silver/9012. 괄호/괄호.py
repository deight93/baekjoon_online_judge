import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in input_list:
    for j in range(len(i)//2):
        i = i.replace("()", "")
    if i != "":
        print("NO")
    else:
        print("YES")
