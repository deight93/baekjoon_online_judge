input_list = [int(i) for i in input().split(" ")]

a = 0
cnt = 0
while True:
    cnt += 1
    a += cnt

    if a >= 1000:
        break

temp_list = []
for i in range(1, cnt+1):
    for j in range(i):
        temp_list += [i]

print(sum(temp_list[input_list[0]-1:input_list[1]]))