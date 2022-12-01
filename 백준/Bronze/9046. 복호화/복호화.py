import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a = sys.stdin.readline().rstrip().replace(" ", "")
    temp = []
    for i in set(a):
        temp += [(i, a.count(i))]
    max_ap = max(temp, key=lambda x: x[1])
    temp_max_cnt = sum([1 if i[1] == max_ap[1] else 0 for i in temp])

    if temp_max_cnt > 1:
        print("?")
    else:
        print(max_ap[0])

