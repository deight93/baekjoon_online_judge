import sys

n = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

total = []
for i in input_list:
    if len(set(i)) == 1:
        total += [50000+(i[0]*5000)]
    elif len(set(i)) == 2:
        set_i = sorted(list(set(i)))
        a = i.count(set_i[0])
        b = i.count(set_i[1])

        if a == 3 and b == 1:
            total += [10000+((set_i[0])*1000)]
        elif b == 3 and a == 1:
            total += [10000+((set_i[1])*1000)]
        elif a == 2 and b == 2:
            total += [2000+((set_i[0])*500)+((set_i[1])*500)]
    elif len(set(i)) == 3:
        set_i = sorted(list(set(i)))
        a = i.count(set_i[0])
        b = i.count(set_i[1])
        c = i.count(set_i[2])
        if a == 2:
            total +=[1000+((set_i[0])*100)]
        elif b == 2:
            total += [1000+((set_i[1])*100)]
        elif c == 2:
            total += [1000 + ((set_i[2]) * 100)]
    else:
        total += [max(i)*100]

print(max(total))