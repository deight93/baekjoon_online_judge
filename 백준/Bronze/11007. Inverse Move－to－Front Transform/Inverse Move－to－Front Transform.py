import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    an = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    s = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    temp = ""
    for j in an:
        temp_an = s[j]
        temp += temp_an
        s.remove(temp_an)
        s.insert(0, temp_an)
    print(temp)

