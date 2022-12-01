while True:
    try:
        a, b = map(int, input().rstrip().split(" "))
        print("{:.2f}".format(a/b))
    except EOFError:
        break