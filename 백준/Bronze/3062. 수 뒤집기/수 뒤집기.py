import sys

t = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(t)]

for i in input_list:
    temp = str(i+int(str(i)[::-1]))

    a = "YES"
    for i in range(len(temp)//2):
        if temp[i] != temp[-1*(i+1)]:
            a = "NO"

    print(a)