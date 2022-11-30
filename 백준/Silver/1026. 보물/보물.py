import sys

n = int(sys.stdin.readline().rstrip())
input_list1 = list(map(int, sys.stdin.readline().rstrip().split(" ")))
input_list2 = list(map(int, sys.stdin.readline().rstrip().split(" ")))
print(sum(map(lambda x:x[0]*x[1], list(zip(sorted(input_list1), sorted(input_list2, reverse=True))))))