import sys

chr_dict = {" ": 0}
for i in range(65, 91):
    chr_dict[chr(i)] = i-64

while True:
    temp = sys.stdin.readline().rstrip()
    if temp == "#":
        break
    else:
        total = 0
        for i in range(1, len(temp)+1):
            total += i*chr_dict[temp[i-1]]
        print(total)