import sys

input_list = [[i, int(sys.stdin.readline().rstrip())] for i in range(8)]
temp = sorted(input_list, key=lambda x: x[1], reverse=True)[:5]

print(sum(map(lambda x: x[1], temp)))
temp2 = sorted(map(lambda x: x[0]+1, temp))
temp_str = ""
for i in temp2:
    temp_str += str(i)+" "
print(temp_str)