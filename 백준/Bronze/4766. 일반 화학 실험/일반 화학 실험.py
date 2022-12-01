import sys

input_list = []
while True:
    n = float(sys.stdin.readline().rstrip())
    if int(n) == 999:
        break
    else:
        input_list += [n]

for i in range(1, len(input_list)):
    print("{:.2f}".format(input_list[i]-input_list[i-1]))