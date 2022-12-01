temp = []
while True:
    try:
        temp += [input()]
    except EOFError:
        break

for i in temp:
    upper = 0
    lower = 0
    num = 0
    space = 0

    for c in i:
        if c.islower():
            lower += 1
        if c.isupper():
            upper += 1
        if c.isnumeric():
            num += 1
        if c.isspace():
            space += 1

    print(lower, upper, num, space)