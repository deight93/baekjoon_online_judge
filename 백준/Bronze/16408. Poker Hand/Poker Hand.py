
import sys

a = [i[0] for i in sys.stdin.readline().rstrip().split(" ")]
set_a = set(a)
str_a = "".join(a)
print(max([str_a.count(i) for i in set_a]))

