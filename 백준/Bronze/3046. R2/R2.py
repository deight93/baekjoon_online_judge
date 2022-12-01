import sys

input_list = [int(i) for i in sys.stdin.readline().split(" ")]

R1 = input_list[0]
S = input_list[1]

R2 = (2*S)-R1
print(R2)