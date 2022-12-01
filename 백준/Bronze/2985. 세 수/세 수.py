import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))

if a == b-c:
    print("{}={}-{}".format(a, b, c))
elif a == b+c:
    print("{}={}+{}".format(a, b, c))
elif a == b*c:
    print("{}={}*{}".format(a, b, c))
elif a == b/c:
    print("{}={}/{}".format(a, b, c))
elif c == a-b:
    print("{}-{}={}".format(a, b, c))
elif c == a+b:
    print("{}+{}={}".format(a, b, c))
elif c == a/b:
    print("{}/{}={}".format(a, b, c))
elif c == a*b:
    print("{}*{}={}".format(a, b, c))