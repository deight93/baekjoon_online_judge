temp = []
for i in range(10):
    n = int(input())

    m = n % 42
    temp += [m]
print(len(set(temp)))