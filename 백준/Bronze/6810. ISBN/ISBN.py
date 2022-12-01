
import sys

input_list = [str(sys.stdin.readline().rstrip()) for i in range(3)]

s = "9780921418"+"".join(input_list)

t = 0
for k, v in enumerate(s):
    if k % 2 == 0:
        t += int(v)*1
    else:
        t += int(v)*3

print("The 1-3-sum is {}".format(t))