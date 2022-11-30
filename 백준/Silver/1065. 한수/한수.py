c = int(input())

cnt = 0
for i in range(1, c+1):
    temp = set()
    k = int(str(i)[0])
    if i < 10:
        temp.add(k)
    for j in str(i)[1:]:
        d = k - int(j)
        temp.add(d)
        k = int(j)
    if len(temp) == 1:
        cnt += 1

print(cnt)
