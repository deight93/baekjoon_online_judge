import sys

a = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
total = a[0]*a[1]
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
print(" ".join([str(i-total) for i in input_list]))