a = input()
b = input()

int_a = int(a)
int_b = int(b)

for i in range(len(b)):
    int_split_b = int(b[len(b)-1-i])
    print(int_a*int_split_b)
print(int_a*int_b)