import sys

t = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(t)]

a = sum([i for i in range(65, 91)])

for i in input_list:
    b = a
    i = list(set(i))
    for j in i:
        b -= ord(j)
    print(b)