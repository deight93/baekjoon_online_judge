import sys

t = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for i in range(t)]

for i in input_list:
    for j in range(0, int(i**0.5)+1):
        temp = int(i**0.5)-j
        if temp+temp**2 <= i:
            print(temp)
            break