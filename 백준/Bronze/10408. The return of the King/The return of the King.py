import sys

s = sys.stdin.readline().rstrip()

ten_c = s.count("10")
new_s = s.replace("10", "")
temp = 10*ten_c

for i in new_s:
    temp += int(i)
print("{:.2f}".format(temp/(len(new_s)+ten_c)))
