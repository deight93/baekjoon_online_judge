import sys

input_list = [sys.stdin.readline().rstrip() for i in range(3)]
a, b, c = map(int, input_list)

t = str(a*b*c)

for i in range(10):
    print(t.count(str(i)))