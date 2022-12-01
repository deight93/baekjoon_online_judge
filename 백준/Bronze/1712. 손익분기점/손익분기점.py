input_list = [int(i) for i in input().split(" ")]

if input_list[1] < input_list[2]:
    cnt = int(input_list[0]/(input_list[2]-input_list[1]))+1
    print(cnt)
else:
    print(-1)