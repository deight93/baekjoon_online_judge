c = int(input())
for i in range(c):
    input_list = [int(i) for i in input().split(" ")]
    x = input_list[0]
    y = input_list[1]
    d = y - x
    root_d = int(d**0.5)

    if d == 1:
        cnt = 1
        print(cnt)
    else:
        if root_d*root_d == d:
            cnt = root_d + root_d - 1
            print(cnt)
        elif root_d*root_d < d <= root_d*(root_d+1):
            cnt = root_d + (root_d + 1) - 1
            print(cnt)
        elif root_d*(root_d+1) < d <= (root_d+1)*(root_d+1):
            cnt = (root_d+1)+(root_d+1) - 1
            print(cnt)