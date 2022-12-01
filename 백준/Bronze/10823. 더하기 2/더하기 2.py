temp = ""
while True:
    try:
        temp += input().rstrip()
    except EOFError:
        break

print(sum(map(int, temp.split(","))))