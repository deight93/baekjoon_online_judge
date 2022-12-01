import sys

a = "1 1 2 2 2 8".split(" ")
input_list = sys.stdin.readline().rstrip().split(" ")
print(" ".join([str(int(i[0])-int(i[1])) if len(set(i)) != 1 else "0" for i in list(zip(a, input_list))]))