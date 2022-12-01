init = int(input())
a = 0
b = 1
num = 0
for i in range(init):
    k = a + b
    a = b
    b = k
print(a)
