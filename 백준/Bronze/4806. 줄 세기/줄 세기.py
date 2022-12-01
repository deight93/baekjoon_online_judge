temp = []
while True:
    try:
        temp += [input()]
    except EOFError:
        break

print(len(temp))