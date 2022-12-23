import sys
import re

n = int(sys.stdin.readline().rstrip())
w = sys.stdin.readline().rstrip()

a = len(re.findall("security", w))
b = len(re.findall("bigdata", w))

if a > b:
    print("security!")
elif a < b:
    print("bigdata?")
else:
    print("bigdata? security!")


