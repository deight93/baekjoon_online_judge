import sys

input_list = [int(sys.stdin.readline().rstrip()) for i in range(3)]

if sum(input_list) == 180:
    if len(set(input_list)) == 3:
        print("Scalene")
    elif len(set(input_list)) == 2:
        print("Isosceles")
    elif len(set(input_list)) == 1:
        print("Equilateral")
else:
    print("Error")