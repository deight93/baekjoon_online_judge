input_year = int(input())

if (divmod(input_year, 4)[1] == 0 and divmod(input_year, 100)[1] != 0) or divmod(input_year, 400)[1] == 0:
    print(1)
else:
    print(0)