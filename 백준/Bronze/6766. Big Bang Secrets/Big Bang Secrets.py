import sys

k = int(sys.stdin.readline().rstrip())
w = sys.stdin.readline().rstrip()

p = 0
r = ""
for i in w:
    p += 1
    s = (3*p)+k
    if ord(i)-s < 65:
        r += chr(91-(65-(ord(i)-s)))
    else:
        r += chr(ord(i) - s)

print(r)
