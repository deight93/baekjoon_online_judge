import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]
temp = {}

for i in input_list:
    if i[0] in temp.keys():
        temp[i[0]] += 1
    else:
        temp[i[0]] = 1

total = ""
for k, v in temp.items():
    if v >= 5:
        total += k

if not total:
    print("PREDAJA")
else:
    print("".join(sorted(total)))