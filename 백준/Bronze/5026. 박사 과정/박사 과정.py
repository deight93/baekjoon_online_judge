import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in input_list:
    if "+" in i:
        print(sum(map(int, i.split("+"))))
    else:
        print("skipped")