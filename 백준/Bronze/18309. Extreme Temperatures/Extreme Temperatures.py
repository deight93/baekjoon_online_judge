min_n = 50
max_n = -50
while True:
    try:
        a = list(map(int, input().split(" ")[1:]))
        min_n = min(min_n, min(a))
        max_n = max(max_n, max(a))
    except EOFError:
        print(min_n, max_n)
        break

