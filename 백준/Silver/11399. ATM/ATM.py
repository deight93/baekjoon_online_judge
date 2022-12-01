import sys

n = int(sys.stdin.readline())
input_list = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

total = 0
for i in range(1, len(input_list)+1):
    total += sum(input_list[:i])
print(total)