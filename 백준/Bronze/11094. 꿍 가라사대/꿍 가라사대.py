
import sys

n = int(sys.stdin.readline().rstrip())
input_list = [sys.stdin.readline().rstrip() for i in range(n)]

for i in input_list:
    if i.find("Simon says") != -1:
        print(i.split("Simon says")[1])