tmp_list = [int(i) for i in input().split(" ")]

a = max(tmp_list)
b = min(tmp_list)

gcd = 0
lcm = 0

while True:
    if a % b == 0:
        gcd = b
        lcm = b

        break
    else:
        c = a % b
        a = b
        b = c


for i in tmp_list:
    lcm = lcm * int(i / gcd)

print(gcd)
print(lcm)