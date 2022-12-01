import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

cnt = 0
for i in range(len(input_list)):
    for j in range(i+1, len(input_list)):
        if input_list[i]+input_list[j] == m:
            cnt += 1

print(cnt)