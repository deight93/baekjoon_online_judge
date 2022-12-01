
import sys

input_list = [sys.stdin.readline().rstrip().split(" ") for i in range(int(sys.stdin.readline().rstrip()))]
print(min(input_list, key=lambda x: x[1])[0])
