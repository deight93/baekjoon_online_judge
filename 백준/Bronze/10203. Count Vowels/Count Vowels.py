import sys

n = int(sys.stdin.readline().rstrip())

v = "aeiou"
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    cnt = 0
    for i in w:
        if i in v:
            cnt += 1
    print("The number of vowels in {} is {}.".format(w, cnt))

