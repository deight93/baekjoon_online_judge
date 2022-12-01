
import sys

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
N = input_list[0]
B = input_list[1]

temp = {}
for i in range(65, 91):
    temp[i-55] = chr(i)

s = ""
while True:
    q = N // B
    r = N % B
    if r > 9:
        s += str(temp[r])
    else:
        s += str(r)

    if q != 0:
        N = q
    else:
        break

print(s[::-1])