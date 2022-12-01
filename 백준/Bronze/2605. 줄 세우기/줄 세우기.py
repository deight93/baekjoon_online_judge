
import sys

n = int(sys.stdin.readline().rstrip())
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

temp = []
for k, i in enumerate(input_list):
    temp.insert(i, k+1)
temp.reverse()
print(" ".join([str(i) for i in temp]))