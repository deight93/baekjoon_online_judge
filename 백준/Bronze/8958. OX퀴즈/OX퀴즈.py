c = int(input())
for i in range(c):
    input_ox = input()
    c = 0
    total_c = 0
    for i in input_ox:
        if i == "O":
            c += 1
            total_c += c
        else:
            c = 0
    print(total_c)