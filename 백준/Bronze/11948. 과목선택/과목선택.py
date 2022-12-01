import sys

input_list = [int(sys.stdin.readline().rstrip()) for _ in range(6)]
a = sorted(input_list[:4], reverse=True)[:3]
b = sorted(input_list[4:], reverse=True)[0]
a.append(b)
print(sum(a))