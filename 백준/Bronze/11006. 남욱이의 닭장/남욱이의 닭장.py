import sys

n = int(sys.stdin.readline())

for _ in range(n):
    input_list = sys.stdin.readline().rstrip().split(" ")
    a, b = map(int, input_list)
    for i in range(0, b+1):
        if i+(2*(b-i)) == a:
            print(i, b-i)
            break
