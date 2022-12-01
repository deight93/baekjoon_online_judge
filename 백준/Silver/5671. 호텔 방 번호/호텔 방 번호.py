while True:
    try:
        a, b = map(int, input().rstrip().split(" "))

        total = 0
        for i in range(a, b+1):
            if len(str(i)) == len(set(str(i))):
                total += 1
        print(total)
    except EOFError:
        break