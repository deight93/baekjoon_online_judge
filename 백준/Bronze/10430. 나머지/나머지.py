input_int = [int(i) for i in input().split(" ")]

A=input_int[0]
B=input_int[1]
C=input_int[2]

print((A+B)%C)
print( ((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)