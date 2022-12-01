n = int(input())
temp = []

for x in range(0, 1001):
    y = (n - 5*x)/3
    if y >= 0 and y.is_integer():
        temp += [x+int(y)]

if not temp:
    print(-1)
else:
    print(min(temp))