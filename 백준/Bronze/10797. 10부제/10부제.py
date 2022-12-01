
import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(input_list.count(n))