import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().split("-") for _ in range(n)]

for i in input_list:
    temp = 0
    for k, j in enumerate(i[0]):
        temp += (ord(j) - 65)*26**(len(i[0])-k-1)
    if abs(temp-int(i[1])) <= 100:
        print("nice")
    else:
        print("not nice")