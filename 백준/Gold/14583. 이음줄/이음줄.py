import sys

h, v = map(float, sys.stdin.readline().rstrip().split(" "))

# 피타고라스
d = (h**2+v**2)**0.5

# 각의 이등분선
a = v*(h/(h+d))
b = v*(d/(h+d))
c = (a**2+h**2)**0.5

# 평행사변형의 넓이
k = (b * h) / c
print("{:.2f} {:.2f}".format(c/2, k))

