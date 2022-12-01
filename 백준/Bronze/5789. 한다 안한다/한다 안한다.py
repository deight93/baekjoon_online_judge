import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in input_list:
    a = len(i)//2
    if i[a-1] == i[a]:
        print("Do-it")
    else:
        print("Do-it-Not")