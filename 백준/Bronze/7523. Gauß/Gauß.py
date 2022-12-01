import sys

n = int(sys.stdin.readline())
input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

for k, i in enumerate(input_list):
    print("Scenario #{}:".format(k+1))
    temp_len = i[1]+(-1*i[0])+1
    if temp_len % 2 == 0:
        temp = (i[1]+i[0]) * (temp_len//2)
    else:
        temp = (i[1] + i[0]) * (temp_len // 2) + ((i[1] + i[0])//2)
    print(temp)
    if k+1 != len(input_list):
        print()