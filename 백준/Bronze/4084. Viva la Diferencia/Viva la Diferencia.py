
import sys

while True:
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    a, b, c, d = input_list
    n = 0
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    elif len(set(input_list)) == 1:
        print(n)
    else:
        while True:
            n += 1
            temp_a = abs(a-b)
            temp_b = abs(b-c)
            temp_c = abs(c-d)
            temp_d = abs(d-a)
            a = temp_a
            b = temp_b
            c = temp_c
            d = temp_d

            if len(set(list([a, b, c, d]))) == 1:
                print(n)
                break