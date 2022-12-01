import sys
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
R, C, ZR, ZC = input_list[0], input_list[1], input_list[2], input_list[3]
input_list2 = [sys.stdin.readline().rstrip() for i in range(R)]

out_put_list = ["" for i in range(R*ZR)]

for i in range(R*ZR):
    for j in range(C):
        out_put_list[i] += input_list2[i//ZR][j]*ZC

for i in out_put_list:
    print(i)