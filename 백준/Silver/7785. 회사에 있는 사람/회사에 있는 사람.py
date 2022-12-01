import sys

n = int(sys.stdin.readline())

input_list = []
for _ in range(n):
    a = sys.stdin.readline().rstrip().split(" ")
    if a[1] == "enter":
        input_list.append(a[0])
    else:
        input_list.remove(a[0])

input_list.sort(reverse=True)
[print(i) for i in input_list]