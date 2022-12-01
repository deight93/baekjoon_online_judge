import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n, -1, -1):
    if i > 1:
        if i-1 == 1:
            n2 = "1 bottle"
        else:
            n2 = "{} bottles".format(i-1)
        print("""{} bottles of beer on the wall, {} bottles of beer. 
Take one down and pass it around, {} of beer on the wall.""".format(i, i, n2))
        print()
    elif i == 1:
        print("""1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.""")
        print()
    else:
        if n == 1:
            n2 = "1 bottle"
        else:
            n2 = "{} bottles".format(n)
        print("""No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {} of beer on the wall.""".format(n2))

