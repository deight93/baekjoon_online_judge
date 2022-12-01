temp = set(range(1, 10000))
temp_set = set()  # 생성자가 있는 숫자 set

for n in temp:
    for i in str(n):
        n += int(i)
    temp_set.add(n)  # add: 집합에 요소를 추가할 때

for j in sorted(temp-temp_set):
    print(j)