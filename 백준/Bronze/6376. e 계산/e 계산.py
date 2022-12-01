import math

print("n e")
print("- -----------")

for i in range(10):
    total = 0
    for j in range(i+1):
        e = 1/math.factorial(j)
        total += e
    if i < 2:
        print('{} {:.0f}'.format(i, total))
    elif i == 2:
        print('{} {:.1f}'.format(i, total))
    else:
        print('{} {:.9f}'.format(i, total))