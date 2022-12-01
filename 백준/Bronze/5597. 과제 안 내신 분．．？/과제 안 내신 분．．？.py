import sys

input_list = [int(sys.stdin.readline().rstrip()) for i in range(28)]
temp = [i for i in range(1, 31)]

for i in sorted(list(set(temp) - set(input_list))):
    print(i)