import sys

input_list = [i for i in sys.stdin.readline().rstrip()]

ck = 1
for i in range(len(input_list)//2):
    if input_list[i] == input_list[len(input_list)-i-1]:
        pass
    else:
        ck = 0
        break

print(ck)