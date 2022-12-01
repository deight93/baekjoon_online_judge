c = int(input())
for i in range(c):
    k = ""
    l = c-i
    for j in range(1, c+1):
        if l > j:
            k += " "
        else:
            k += "*"
    print(k)