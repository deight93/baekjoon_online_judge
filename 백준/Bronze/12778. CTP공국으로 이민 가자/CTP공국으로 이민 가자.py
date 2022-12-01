
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n = sys.stdin.readline().rstrip().split(" ")
    input_list = sys.stdin.readline().rstrip().split(" ")

    if n == "C":
        print(" ".join([str(ord(i)-64) for i in input_list]))
    else:
        print(" ".join([chr(int(i)+64) for i in input_list]))

