import sys
c = int(sys.stdin.readline())

count_list = [0 for i in range(10000+1)]
for i in range(c):
    count_list[int(sys.stdin.readline())] += 1

for i in range(1, 10000+1):
    for j in range(count_list[i]):
        sys.stdout.write(str(i) + "\n")