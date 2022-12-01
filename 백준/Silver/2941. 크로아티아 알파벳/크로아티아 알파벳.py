temp = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

c = input()

for i in temp:
    if c.find(i) != -1:
        c = c.replace(i, " ")

print(len(c))