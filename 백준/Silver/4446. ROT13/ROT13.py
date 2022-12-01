
import sys

a = "a i y e o u".split(" ")
A = "a i y e o u".upper().split(" ")
a2 = a[3:] + a[:3]
A2 = A[3:] + A[:3]
b = "b k x z n h d c w g p v j q t s r l m f".split(" ")
B = "b k x z n h d c w g p v j q t s r l m f".upper().split(" ")
b2 = b[10:] + b[:10]
B2 = B[10:] + B[:10]

a_list = list(zip(a, a2))+list(zip(A, A2))+list(zip(b, b2))+list(zip(B, B2))
a_dict = {}
for i in a_list:
    a_dict[i[0]] = i[1]

n = sys.stdin.readlines()

r_list = []
for j in n:
    j = j.rstrip()
    r = ""
    for i in j:
        if i.isalpha():
            r += a_dict[i]
        else:
            r += i
    r_list.append(r)

for i in r_list:
    print(i)