import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in input_list:
    temp = []
    temp += [str(i // 25)]
    i -= ((i // 25)*25)
    temp += [str(i // 10)]
    i -= ((i // 10)*10)
    temp += [str(i // 5)]
    i -= ((i // 5)*5)
    temp += [str(i // 1)]
    print(" ".join(temp))