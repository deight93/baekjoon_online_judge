input_list = [int(i) for i in input().split(" ")]
h = input_list[0]
m = input_list[1]

if m-45 < 0:
    if h-1 < 0:
        print_h = 23
    else:
        print_h = h-1
    print_m = 60 + m - 45
else:
    print_h = h
    print_m = m - 45

print(print_h, print_m)