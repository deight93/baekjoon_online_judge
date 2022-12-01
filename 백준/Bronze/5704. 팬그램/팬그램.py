import sys

while True:
    input_list = sys.stdin.readline().rstrip()
    if input_list == "*":
        break
    temp = [chr(i) for i in range(97, 123)]
    ck = list(set(temp)-set(input_list))
    if not ck:
        print("Y")
    else:
        print("N")