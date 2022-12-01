import sys

n = int(sys.stdin.readline().rstrip())
input_list = [input().lower() for _ in range(n)]

for i in input_list:
    if len(i) % 2 == 0:
        if i[:len(i)//2] == str(i[len(i)//2:])[::-1]:
            print("Yes")
        else:
            print("No")
    else:
        if i[:len(i)//2+1] == str(i[len(i)//2:])[::-1]:
            print("Yes")
        else:
            print("No")